# SQL_TABLE_RULES.md — Guía principal de tablas y reglas de consulta

Fecha de corte: 2026-05-21  
Proyecto: Legasys Web

## Objetivo

Este archivo sirve para que un bot o asistente que consulta la base de datos de Legasys no haga SQL “genérico”, sino SQL alineado con la lógica real del sistema.

No basta con conocer nombres de tablas. En Legasys muchos datos:

- viven en más de una tabla posible
- tienen prioridad funcional
- dependen del módulo (`Legal` vs `Operaciones`)
- dependen de la notaría (`CO_COMP`)
- o dependen de estructuras dinámicas (`H_CODO`, `R_CODO_KARD`, etc.)

## Regla cero

Antes de armar una consulta, el bot debe decidir:

1. qué módulo está consultando
2. cuál es la notaría (`CO_COMP`)
3. si el dato es físico/directo o funcional/derivado
4. si el dato viene del ticket, del trámite, del participante, del cliente, del documento dinámico o de la liquidación
5. qué tipo de fecha quiere realmente el usuario

## Reglas globales

### 1. Multinotaría

Siempre que la tabla tenga `CO_COMP`, debe filtrarse por la notaría correcta.

Regla práctica:

- en la app web: usar `legasys_user('CO_COMP')`
- en SQL externo: pedir explícitamente `CO_COMP`

Nunca mezclar registros de distintas notarías.

### 2. Legal vs Operaciones

Hay dos formas funcionales de distinguirlos:

- `P_TICK.CO_MODU`
  - `1` = Legal (Protocolar)
  - `2` = Operaciones (Extraprotocolar)

- `P_TRAM.IN_KARD`
  - `1` = Legal / tiene kardex
  - `0` o `NULL` = Operaciones / sin kardex

Regla recomendada:

- para pantallas o tickets: suele ser más claro `P_TICK.CO_MODU`
- para participantes y prioridad de uso del trámite: suele ser más útil `P_TRAM.IN_KARD`

### 3. Tablas `_type`

Las tablas legacy con sufijo `_type` deben respetar exactamente su nombre real.

Ejemplos correctos:

- `A_ETAP_TRAM_type`
- `A_TIPO_CAMP_type`

No convertirlas a mayúsculas tipo `..._TYPE`.

### 4. Datos funcionales vs columnas históricas

No asumir que “la columna que parece correcta” es la fuente oficial.

Ejemplos reales:

- una fecha puede venir de `P_TRAM.FE_ESCR_TRAM` o de un dinámico `H_CODO`
- un cliente puede venir de `P_CLIE` o del participante marcado como cliente en `R_PRTC_TRAM`
- un usuario responsable puede venir de `CO_USUA_ABOG` o `CO_USUA_MODI`

Siempre aplicar la prioridad funcional del módulo.

### 5. Rango de fechas ambiguo y regla de Operaciones

Si el usuario da un rango de fechas pero no dice qué fecha quiere usar, el bot debe pedir aclaración antes de construir el SQL.
Las preguntas mínimas válidas son:
- fecha de creación del ticket / kardex
- fecha de escritura / instrumento
- fecha de firma
- fecha de caja / cobro

No asumir una fecha por defecto cuando la consulta depende del rango.

**REGLA CRÍTICA PARA OPERACIONES:**
El módulo de Operaciones (`CO_MODU = 2`) **NO tiene fecha de firma (`FE_FIRM_COMP`) ni fecha de instrumento (`FE_ESCR_TRAM`)**. Para Operaciones, la única fecha transaccional válida es la fecha de ticket (`P_TICK.FE_CREA_TICK`). 
Si el usuario pide un reporte mezclado (Legal + Operaciones) usando "fecha de firma", el bot debe advertir que Operaciones no entrará en ese filtro o debe adaptar el SQL para usar `FE_CREA_TICK` para los de Operaciones.

### 6. Caja: separar cobro directo, facturado y cobranza

No mezclar estas rutas como si fueran la misma cosa:

- cobro directo / pagado normal:
  - `P_CABE_CAJA`
  - fecha principal: `FE_CABE_CAJA`
  - estado usual: `IN_ESTA_CAJA = 6`

- facturado / al crédito:
  - `P_CABE_CAJA`
  - fecha principal: `FE_CABE_CAJA`
  - estado usual: `IN_ESTA_CAJA = 5`

- cobranza de créditos:
  - `R_CAJA_PAGO -> P_PAGO_DOCU -> P_CABE_CAJA`
  - fecha principal: `P_PAGO_DOCU.FE_PAGO_DOCU`

Si el usuario pide “pagados”, normalmente empezar por `IN_ESTA_CAJA = 6`.
Si pide mezclar cancelados con facturados o cobranza, el bot debe explicitar qué ruta está usando.

### Campos clave de `P_CABE_CAJA`

| Campo | Significado |
|---|---|
| `CO_USUA_MODI` | **Usuario que GENERÓ/emitió el comprobante.** Es el campo correcto para saber qué personal de la notaría creó el cobro. NUNCA uses `CO_USUA_ACTI` para esto. |
| `CO_USUA_ACTI` | ~~No se usa en la práctica~~. Ignorar este campo completamente. |
| `CO_USUA_ANUL` | Código del usuario que **ANULÓ** el comprobante. |
| `TS_USUA_ANUL` | Fecha/timestamp en que se **ANULÓ** el comprobante. |
| `CO_TIPO_MONE` | Moneda del comprobante: `1` = Soles, `2` = Dólares. |
| `FE_CABE_CAJA` | Fecha principal del comprobante de caja. |
| `MO_BRUT` | **Monto bruto** (sin IGV). |
| `MO_IGV` | **Monto del IGV** (el impuesto). |
| `MO_NETO` | **Monto total** (bruto + IGV). Es el campo a usar cuando se pida el total cobrado. |

| `CO_FORM_PAGO_CAJA` | Código de la **forma de pago** usada en el comprobante. Se cruza con `A_FORM_PAGO_CAJA`. Código especial: `5` = Al crédito. |

**REGLA DE NOTARÍA EN CAJA:**
La tabla `P_CABE_CAJA` **sí tiene** el indicador `CO_COMP`. Por lo tanto, para buscar información de caja de una notaría específica, puedes filtrar directamente usando `P_CABE_CAJA.CO_COMP = {co_comp}`. Esto hace las búsquedas más rápidas y no requiere hacer JOIN con `P_TICK`, `P_TRAM` ni `A_SEMI_TDOC` solo para obtener la notaría.

**REGLA CRÍTICA DE USUARIO EN CAJA:**
Si te piden "quién cobró", "quién generó el ingreso" o "qué personal registró el comprobante", el ÚNICO campo válido es `CO_USUA_MODI`. El campo `CO_USUA_ACTI` **NO SE USA EN LA PRÁCTICA y debe ser ignorado completamente**. Nunca hagas JOIN con él.

### Formas de pago: `A_FORM_PAGO_CAJA`

Esta tabla es el **catálogo de formas de pago** de la notaría. Contiene los códigos (`CO_FORM_PAGO_CAJA`) y sus nombres descriptivos.

**Campos principales:**
- `CO_FORM_PAGO_CAJA` → código de la forma de pago (PK)
- `DE_FORM_PAGO_CAJA` → descripción/nombre visible (ej: "EFECTIVO", "YAPE", "TARJETA", "TRANSFERENCIA")

**Código fijo conocido:**
- `5` = Al crédito (facturado sin cobro inmediato)

**REGLA CRÍTICA DE FORMAS DE PAGO (MUY IMPORTANTE):**
Cuando el usuario pregunte por una forma de pago específica (ej: "yape", "POS", "efectivo", "transferencia", "tarjeta"), **NUNCA asumas el código directamente**. Debes seguir este proceso en 2 pasos:

1. **Paso 1 — Buscar en el catálogo:** Armar un sub-query o lookup previo sobre `A_FORM_PAGO_CAJA` buscando la descripción que más se aproxime al término que usó el usuario. Tener en cuenta alias coloquiales peruanos:
   - El usuario dice "yape" o **"moradito"** → buscar `DE_FORM_PAGO_CAJA LIKE '%YAPE%'`
   - El usuario dice "plin" → buscar `DE_FORM_PAGO_CAJA LIKE '%PLIN%'`
   - El usuario dice "POS", "tarjeta", "visa", "mastercard" → buscar `DE_FORM_PAGO_CAJA LIKE '%TARJET%' OR DE_FORM_PAGO_CAJA LIKE '%POS%'`
   - El usuario dice "transferencia" o "transfe" → buscar `DE_FORM_PAGO_CAJA LIKE '%TRANSF%'`
   - El usuario dice "efectivo" o "cash" → buscar `DE_FORM_PAGO_CAJA LIKE '%EFECTIV%'`
   - El usuario dice "depósito" → buscar `DE_FORM_PAGO_CAJA LIKE '%DEPOS%'`
   - El usuario dice "cheque" → buscar `DE_FORM_PAGO_CAJA LIKE '%CHEQUE%'`

2. **Paso 2 — Filtrar en P_CABE_CAJA:** Con el código encontrado, filtrar `P_CABE_CAJA.CO_FORM_PAGO_CAJA = (código encontrado)`.

**Patrón SQL recomendado:**
```sql
WHERE PC.CO_FORM_PAGO_CAJA IN (
    SELECT CO_FORM_PAGO_CAJA FROM A_FORM_PAGO_CAJA
    WHERE DE_FORM_PAGO_CAJA LIKE '%YAPE%'
)
```

**Excepción:** El código `5` (crédito) sí está hardcodeado y puede usarse directamente sin lookup cuando el usuario pida "al crédito" o "facturado".

---

## Núcleo transaccional

## `P_TICK`

Cabecera principal del ticket.

### Qué representa

- cliente principal del ticket
- módulo del ticket
- notaría
- kardex visible
- referencias de abogado/modificador

### Campos importantes

- `CO_TICK_CONT` → PK cabecera del ticket
- `CO_CLIE` → cliente del ticket
- `CO_COMP` → notaría
- `CO_MODU` → módulo (`1 legal`, `2 operaciones`)
- `NU_KARD` → número de kardex visible
- `FE_CREA_TICK` → fecha del ticket / fecha de kardex funcional en muchas consultas
- `CO_USUA_ABOG` → abogado/responsable principal si aplica
- `CO_USUA_MODI` → respaldo de usuario responsable

### Reglas

- el kardex visible se toma normalmente desde `P_TICK.NU_KARD`
- si la consulta pide “usuario responsable”, priorizar:
  1. `CO_USUA_ABOG`
  2. si está vacío o `0`, `CO_USUA_MODI`

## `R_TICK_SERV`

Relación entre ticket y servicio principal.

### Qué representa

- vínculo entre `P_TICK` y `P_TRAM`
- estado funcional de algunos procesos asociados al servicio

### Campos importantes

- `CO_TICK_CONT`
- `CO_TICK_SERV`
- `CO_SERV_ALTE`
- `IN_FIRM_COMP`
- `FE_FIRM_COMP`

### Reglas

- **OBLIGATORIO:** Siempre que uses esta tabla en un JOIN o consulta, DEBES aplicar el filtro `R_TICK_SERV.IN_ESTA = 1`.
- si la consulta pide fecha de firma, usar `R_TICK_SERV.FE_FIRM_COMP`
- no confundir fecha de firma con:
  - `P_TICK.FE_CREA_TICK` (fecha de ticket / kardex)
  - `P_TRAM.FE_ESCR_TRAM` (fecha de instrumento)
- **CUIDADO CON CO_SERV_ALTE:** Esta columna **NO es** una llave foránea hacia `P_SERV.CO_SERV`. Apunta a `H_SERV_ALTE` (servicios alternos). Si necesitas obtener el servicio principal (`P_SERV`) a partir de un ticket, **NUNCA cruces R_TICK_SERV directamente con P_SERV**. Debes pasar obligatoriamente por `P_TRAM` así: `R_TICK_SERV.CO_TICK_SERV = P_TRAM.CO_TICK_SERV` y luego `P_TRAM.CO_SERV = P_SERV.CO_SERV`.

### Join base más común

```sql
P_TICK.CO_TICK_CONT = R_TICK_SERV.CO_TICK_CONT
P_TRAM.CO_TICK_SERV = R_TICK_SERV.CO_TICK_SERV
P_SERV.CO_SERV = P_TRAM.CO_SERV
```

## `P_TRAM`

Trámite principal del servicio.

### Qué representa

- servicio real del trámite
- instrumento
- etapa
- año del trámite
- control documental

### Campos importantes

- `CO_TICK_SERV`
- `CO_SERV`
- `CO_COMP`
- `CO_ETAP_TRAM`
- `NU_ANIO_TRAM`
- `NU_INST`
- `FE_ESCR_TRAM`
- `NU_CTRL`
- `IN_KARD`

### Reglas

- `NU_INST` = número de instrumento
- `NU_CTRL` = número de control
- `IN_KARD = 1` marca trámites Legal
- para Operaciones suele venir `0` o `NULL`
- en algunas consultas documentales la fecha real no debe depender solo de `FE_ESCR_TRAM`; revisar si el módulo usa dinámicos

## `P_SERV`

Catálogo de servicios.

### Campos importantes

- `CO_SERV`
- `DE_SERV`
- `CO_REGI_NOTA`
- `IN_ESTA`

### Reglas

- `CO_REGI_NOTA` es clave para conectar el servicio con:
  - `R_REGI_NOTA`
  - `A_DOCU_FIRM`
  - y los dinámicos documentales de escritura

---

## Estructura de cliente y participante

## `P_CLIE`

Cliente del ticket.

### Uso principal

- fuente principal de cliente en el sistema
- cabecera comercial / administrativa del ticket

### Campos frecuentes

- `CO_CLIE`
- `NO_BUSQ`
- `DE_DIRE`

### Regla

- para sacar el cliente, usar siempre la ruta de cliente y no participantes
- base mínima:
  - `P_CLIE`
- complementar, según el dato pedido, con:
  - `H_CLIE_NATU`
  - `H_CLIE_MAIL`
- no usar `R_PRTC_TRAM.IN_CLIE` como fuente de cliente

## `P_PRTC`

Cabecera/base del participante.

### Campos frecuentes

- `CUP`
- `NO_CORT`
- `NS_ULTI_DIRE`

### Regla importante

- `NS_ULTI_DIRE` no siempre debe tratarse como dirección definitiva
- para Legal, la dirección más confiable puede ser la última útil de `H_PRTC_DIRE`

## `H_PRTC_NATU`

Detalle natural del participante.

### Campos frecuentes

- `CUP`
- `NU_DOCU_IDEN`
- `CO_TDOC_IDEN`
- `AP_PATE`
- `AP_MATE`
- `NO_NOMB`
- `CO_ESTA_CIVI`
- `CO_INDI_GENE`
- `FE_NACI_UIF`
- `NU_PART`

### Reglas

- el estado civil del formulario mixto de Operaciones se guarda aquí
- representantes naturales en algunos flujos también guardan aquí `NU_PART`

## `H_PRTC_JURI`

Detalle jurídico del participante.

### Campos frecuentes

- `CUP`
- `NU_RUC`
- `NO_RAZO_SOCI`

## `H_PRTC_DIRE`

Histórico/detalle de direcciones del participante.

### Regla funcional crítica

- en búsquedas de participantes de Legal, si el registro priorizado no trae buena dirección, se debe preferir la última dirección útil de `H_PRTC_DIRE`
- no depender ciegamente de `P_PRTC.NS_ULTI_DIRE`

## `R_PRTC_TRAM`

Relación participante ↔ trámite.

### Qué representa

- qué participantes pertenecen a un trámite
- qué rol cumplen
- qué participante actúa como cliente

### Campos frecuentes

- `CO_TICK_SERV`
- `CUP`
- `CO_TIPO_PRTC`
- `IN_CLIE`
- `IN_ESTA`

### Reglas

- para saber si un participante fue usado en Legal u Operaciones, cruzar:

```sql
R_PRTC_TRAM.CO_TICK_SERV -> P_TRAM.CO_TICK_SERV
```

- para priorizar participantes en Legal:
  1. último uso en `P_TRAM.IN_KARD = 1`
  2. si no existe, último uso en `P_TRAM.IN_KARD = 0/null`
  3. si no existe participante, ir a cliente por `P_CLIE` / `H_CLIE_NATU` / `H_CLIE_MAIL`
  4. si es DNI y faltan datos, usar RENIEC

## `A_TIPO_PRTC`

Catálogo base del tipo de participante.

### Campos funcionales importantes

- `CO_TIPO_PRTC`
- `DE_TIPO_PRTC`
- `CO_TIPO_UIF`
- `CO_TIPO_PDT`
- `CO_INTE_CNL`
- `CO_TIPO_CNL_ULTI`

### Regla

- estos códigos viven en el catálogo base, no en la relación del servicio

## `R_PRTC_SERV`

Relación tipo de participante ↔ servicio.

### Campos importantes

- `CO_PRTC_SERV`
- `CO_TIPO_PRTC`
- `CO_SERV`
- `CO_TIPO_SUNA`
- `CO_TIPO_CNL`
- `NU_ORDE`
- `IN_ESTA`

### Regla

- aquí se guarda la codificación propia del servicio
- no mezclar con los campos de catálogo de `A_TIPO_PRTC`

---

## Liquidación, conceptos y caja

## `P_CPTO`

Catálogo de conceptos financieros.

### Campos frecuentes

- `CO_CPTO`
- `DE_CPTO`
- `IN_ESTA`

## `R_SERV_CPTO_TARI`

Relación servicio ↔ concepto ↔ tarifa.

### Qué representa

- conceptos disponibles para un servicio
- orden de visualización
- monto base / tarifa
- configuración por notaría

### Campos importantes

- `CO_SERV_CPTO_TARI`
- `CO_SERV`
- `CO_CPTO`
- `CO_COMP`
- `CO_TARI`
- `NU_ORDE`
- `IM_TARI`
- `IN_ESTA`

### Reglas críticas

- siempre filtrar por `CO_COMP`
- el orden de conceptos en liquidación debe respetar `NU_ORDE`
- si el usuario usa un concepto libre no relacionado al servicio:
  - debe crearse la relación en esta tabla
  - con monto `0.00`
  - normalmente usando la tarifa base (`CO_TARI = 1` en el flujo descrito)

## `H_SUB_SERV`

Catálogo/registro de subservicios o subconceptos operativos.

### Regla funcional

- en Operaciones, un subservicio puede estar relacionado a un concepto mediante `CO_CPTO`
- no todos los servicios tienen subservicios
- si existen, pueden editarse desde liquidación para cambiar descripción/monto sugerido en `H_PRES_TICK`

## `H_PRES_TICK`

Presupuesto / liquidación del ticket.

### Qué representa

- conceptos cobrables del ticket o trámite
- monto presupuestado, facturado, cobrado, saldo
- detalle funcional visible en caja

### Campos funcionales frecuentes

- `CO_TICK_SERV`
- `CO_CPTO`
- `DE_DETA_CPTO`
- `MO_TRAN_TICK` (Precio base/original)
- `MO_IMPO_TICK` (Saldo pendiente)

### Reglas Críticas de Montos

- `MO_TRAN_TICK`: Representa el **PRECIO ORIGINAL** liquidado para ese concepto. (Ej: Se liquida un servicio por 400 soles -> `MO_TRAN_TICK = 400`). 
  - **REGLA DE SUMA:** Un ticket puede tener varios conceptos (varias filas en `H_PRES_TICK`). Si te preguntan por trámites "no liquidados" o "con liquidación en cero", **NO** debes usar un simple `WHERE MO_TRAN_TICK = 0`. Eso es un error grave porque podrías filtrar una fila gratuita de un ticket que sí tiene otras filas cobradas. Debes agrupar (`GROUP BY`) y usar `HAVING SUM(MO_TRAN_TICK) = 0 OR SUM(MO_TRAN_TICK) IS NULL`.
- `MO_IMPO_TICK`: Representa el **SALDO PENDIENTE**. (Ej: Al principio es 400. Si el cliente paga 100 por caja, este campo bajará a 300). ¡NUNCA uses `MO_IMPO_TICK = 0` para buscar cosas "no liquidadas"! Un `MO_IMPO_TICK = 0` significa que el trámite **fue liquidado y ya está totalmente pagado**.
- el nombre del subconcepto o texto libre se persiste en `DE_DETA_CPTO`
- modificar monto no implica necesariamente modificar el texto
- en Operaciones, si el usuario cambia un subconcepto, debe cambiar la descripción visible y el importe sugerido de esa línea

## `H_DETA_CAJA`

Detalle del comprobante/caja.

### Regla funcional

- `DE_DETA_CAJA` = nombre del servicio
- `DE_DETA_CPTO` = concepto o subconcepto
- si ambos existen y son distintos, el detalle visible puede mostrarse como:

```text
DE_DETA_CAJA - DE_DETA_CPTO
```

## `H_DL939_PAGO`

Medios de pago / pagos relacionados.

### Reglas recientes

- la relación del adjunto al pago vive en `CO_UPDA_DIGI`
- los registros expuestos por IA usan `IN_EXHI = 1`
- si el pago corresponde a subservicio, usar `CO_TICK_SERV_SUB`

---

## Documentos dinámicos y escritura

## `A_DOCU_FIRM`

Catálogo de documentos documentales.

### Campos importantes

- `CO_DOCU_FIRM`
- `CO_REGI_NOTA`
- `DE_DOCU_FIRM`
- `NC_DOCU_FIRM`
- `IN_ESTA`

### Regla

- un mismo `CO_REGI_NOTA` puede tener uno o más `CO_DOCU_FIRM`
- escritura / parte / acta / testimonio dependen de este catálogo

## `H_CODO`

Catálogo de campos dinámicos documentales.

### Campos importantes

- `CO_CODO`
- `CO_DOCU_FIRM`
- `CO_COMP`
- `CO_TIPO_CAMP`
- `DE_CODO`
- `NU_ORDE`
- `NC_CODO`
- `IN_TIPO_CAMP`
- `IN_ESTA`

### Regla

- define los campos de formularios dinámicos de escritura
- el tipo real se interpreta con `A_TIPO_CAMP_type`
- en varios flujos documentales esta tabla es fuente funcional y no simple decoración

## `A_TIPO_CAMP_type`

Catálogo del tipo de campo dinámico.

### Valores conocidos

- `1` = número
- `2` = letras
- `3` = alfanumérico
- `4` = fecha
- `5` = minuta

### Regla

- si se consulta un campo dinámico, su interpretación depende de este catálogo

## `R_CODO_KARD`

Valor concreto de un campo dinámico en un kardex/trámite.

### Qué representa

- relación entre trámite/kardex y `H_CODO`
- valor guardado para ese campo

### Regla

- para recuperar el valor real de un dato dinámico del kardex, suele requerirse:

```sql
R_CODO_KARD.CO_CODO -> H_CODO.CO_CODO
```

### Regla crítica de fecha de escritura

En algunos flujos de escritura, la fecha real del instrumento debe tomarse del dinámico asociado al campo tipo fecha, no solo del nombre textual del campo.

## `R_REGI_NOTA`

Configuración por notaría y tipo de registro notarial.

### Qué representa

- reglas del servicio/documento por notaría
- también participa en formularios de participantes de Operaciones

### Reglas clave

- `IN_INGR_PRTC` en Operaciones debe resolverse primero desde `R_REGI_NOTA`, no desde `P_SERV`
- `IN_INGR_PRTC = 5` = formulario mixto / genérico

## `A_REGI_NOTA`

Catálogo de registros notariales.

### Qué representa

- agrupación semántica de servicios
- familia notarial/documental a la que pertenece un servicio
- base para entender grupos como escrituras, vehiculares, testamentos, protestos, etc.

### Regla funcional clave

- `P_SERV.CO_REGI_NOTA` apunta a `A_REGI_NOTA.CO_REGI_NOTA`
- si la pregunta del usuario es por una familia documental o grupo notarial, el bot debe pensar primero en `CO_REGI_NOTA`
- si la pregunta del usuario es por un servicio exacto, el filtro directo puede hacerse por `CO_SERV`

### Registros notariales de Legal conocidos (`CO_MODU = 1`)

Mapa base actualmente documentado:

- `1` = `REGISTRO DE ESCRITURAS`
- `2` = `REGISTRO DE VEHICULARES`
- `3` = `NO CONTENCIOSOS`
- `4` = `GARANTIAS MOBILIARIAS`
- `5` = `TESTAMENTOS`
- `6` = `PROTESTOS`
- `13` = `REGISTRO DE MINUTAS`
- `14` = `REGISTRO TRAMITES`
- `16` = `REPORTE VEHICULAR`
- `17` = `COPIA CERTIFICADA`

### Cómo debe razonar el bot

Ejemplos:

- si preguntan `solo las transferencias vehiculares`, no asumir de inmediato un único `CO_SERV`; primero evaluar si corresponde el grupo `CO_REGI_NOTA = 2`
- si preguntan `todo lo de escrituras`, priorizar `CO_REGI_NOTA = 1`
- si preguntan `todos los testamentos`, priorizar `CO_REGI_NOTA = 5`

### Advertencia

- no todos los servicios del mismo `CO_REGI_NOTA` significan exactamente lo mismo, pero sí comparten una misma familia funcional
- por eso:
  - preguntas amplias → usar `CO_REGI_NOTA`
  - preguntas puntuales sobre un servicio específico → usar `CO_SERV`

## `Z_KARD_ESCR`

Repositorio documental del kardex.

### Campos funcionales

- `IM_DOCU`
- `IM_DOCU_PDF`

### Regla

- si la UI pregunta si existe documento o PDF, la fuente real es esta tabla
- no depender solo de etapas del trámite

---

## Seguimiento, etapas y estados

## `A_ETAP_TRAM_type`

Catálogo de etapas del trámite.

### Regla

- las etapas se buscan por nombre funcional o por código conocido

## `H_SGMT_TRAM`

Seguimiento del trámite.

### Qué representa

- histórico de etapas / hitos funcionales

### Casos importantes

- `AUTORIZADO IMPRIMIR`
- `INGRESO DE DATOS SERVICIO`
- `INGRESO DE DATOS ESCRITURA`

## `H_SGMT_LOG`

Auditoría detallada del seguimiento.

### Regla

- usar cuando se necesita registrar quién autorizó o qué pasó con detalle, sin alterar la etapa principal

---

## IA, QR y nube

## `H_JSON_TRAM`

Trazabilidad de IA / integraciones documentales.

### Campos funcionales

- `CO_TIPO_API`
  - `1` = Minuta IA
  - `2` = Medio de pago
- `ID_MINU`

### Regla

- `ID_MINU` hoy puede guardar identificadores externos como `id_consulta` o `id_escaneo`

## `P_DOCU_DIGI_QR`
## `H_DOCU_DIGI_QR_PRTC`
## `H_DOCU_DIGI_QR_ESTA`

### Regla

- estas tres estructuras sostienen la publicación y verificación del documento digital con QR
- si una consulta es de verificación pública, debe considerar esas tablas

---

## Consultas base recomendadas

## A. Ticket + trámite + servicio

Cuando se quiera la estructura principal del caso:

```sql
FROM R_TICK_SERV RTS
JOIN P_TICK PT ON PT.CO_TICK_CONT = RTS.CO_TICK_CONT
JOIN P_TRAM TR ON TR.CO_TICK_SERV = RTS.CO_TICK_SERV
JOIN P_SERV PS ON PS.CO_SERV = TR.CO_SERV
```

## B. Kardex legal

Si se parte de un kardex visible:

```sql
WHERE PT.NU_KARD = ?
  AND PT.CO_MODU = 1
  AND PT.CO_COMP = ?
```

## C. Participante del trámite

```sql
FROM R_PRTC_TRAM RPT
JOIN P_PRTC P ON P.CUP = RPT.CUP
LEFT JOIN H_PRTC_NATU N ON N.CUP = P.CUP
LEFT JOIN H_PRTC_JURI J ON J.CUP = P.CUP
```

Luego decidir por lógica:

- si se quiere cliente del trámite: `RPT.IN_CLIE = 1`
- si se quiere el último Legal: cruzar con `P_TRAM.IN_KARD = 1`

## D. Liquidación del trámite

```sql
FROM H_PRES_TICK HPT
```

Complementar con:

- `P_CPTO`
- `R_SERV_CPTO_TARI`

según la necesidad.

## E. Campos dinámicos documentales

```sql
FROM H_CODO HC
JOIN A_TIPO_CAMP_type ATC ON ATC.CO_TIPO_CAMP = HC.CO_TIPO_CAMP
WHERE HC.CO_DOCU_FIRM = ?
```

Si se requieren valores concretos del kardex:

```sql
JOIN R_CODO_KARD RCK ON RCK.CO_CODO = HC.CO_CODO
```

---

## Trampas comunes que el bot debe evitar

1. Usar `P_TRAM.NU_TRAM` como si fuera el kardex visible.
   - REGLA ESTRICTA: NUNCA usamos la columna `NU_TRAM` para ningún reporte ni selección. El kardex visible siempre es `P_TICK.NU_KARD`. Si el usuario pide "kardex", es obligatorio hacer JOIN con P_TICK.

2. Usar `TS_USUA_MODI` como fecha de kardex.
   - Esa suele ser fecha de modificación, no fecha funcional del ticket.

3. No filtrar por `CO_COMP`.

4. Mezclar `A_TIPO_PRTC` con `R_PRTC_SERV`.
   - Catálogo base y codificación por servicio no son lo mismo.

5. Leer documento/PDF desde seguimiento del trámite.
   - La fuente real es `Z_KARD_ESCR`.

6. Suponer que el último participante global siempre es el correcto.
   - En Legal primero debe priorizarse el último uso en Legal.

7. Suponer que todo servicio tiene concepto principal configurado.
   - En liquidación puede haber conceptos libres que obligan a crear relación en `R_SERV_CPTO_TARI` con monto cero.

8. Suponer que `P_CLIE` siempre resuelve al cliente funcional del trámite.
   - A veces el cliente relevante es el participante marcado como cliente.

9. Suponer que `FE_ESCR_TRAM` siempre es la única fecha válida de escritura.
   - En algunos flujos documentales la fecha funcional real viene del dinámico.

10. Consultar tablas `_type` con nombre distinto al real.

---

## Recomendación para prompts del bot SQL

Cuando le preguntes al bot por una consulta, conviene pasarle también:

1. la notaría (`CO_COMP`)
2. si el reporte es de `Legal` o `Operaciones`
3. si “cliente” significa:
   - cliente del ticket
   - o participante cliente del trámite
4. si la fecha es:
   - fecha del ticket
   - fecha de instrumento
   - fecha dinámica del documento
5. si quieres solo datos visibles o también lógica funcional

## Frase recomendada para invocar al bot

```text
Arma el query respetando SQL_TABLE_RULES.md. Usa prioridad funcional real del sistema, no solo nombres de columnas.
```
