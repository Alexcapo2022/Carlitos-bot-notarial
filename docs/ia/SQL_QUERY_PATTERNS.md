# SQL_QUERY_PATTERNS.md — Patrones de consultas frecuentes

Fecha de corte: 2026-05-21  
Proyecto: Legasys Web

## Objetivo

Este archivo le da al bot ejemplos de cómo pensar queries comunes sin inventar joins.

No pretende ser un catálogo exhaustivo de SQL final, sino una guía de estructura.

## Regla general

Antes de escribir el query, definir:

1. si la pregunta es de Legal, Operaciones o Caja
2. si el dato está a nivel ticket, trámite, participante, concepto o documento
3. si el usuario pregunta por un servicio exacto (`CO_SERV`) o por una familia (`CO_REGI_NOTA`)
4. qué fecha quiere usar realmente

## Regla operativa de fechas

Si la consulta necesita tiempo, el bot debe validar:

1. si el usuario ya dio rango de fechas
2. si no lo dio y el reporte lo necesita, pedir el rango
3. si dio un rango, confirmar a qué tipo de fecha aplica:
   - fecha de creación del ticket / kardex
   - fecha de escritura / instrumento
   - fecha de firma
   - fecha de caja / cobro

No asumir una fecha por defecto si la pregunta es ambigua.

---

## Patrón 1 — Kardex creados

Pregunta típica:

```text
¿Cuántos kardex se crearon en mayo 2026?
```

Pensamiento:

- kardex visible = `P_TICK.NU_KARD`
- fecha de kardex = `P_TICK.FE_CREA_TICK`
- Legal = `P_TICK.CO_MODU = 1`

Base:

```sql
FROM P_TICK PT
WHERE PT.CO_MODU = 1
  AND PT.NU_KARD IS NOT NULL
  AND PT.FE_CREA_TICK >= ?
  AND PT.FE_CREA_TICK < ?
```

---

## Patrón 2 — Kardex escriturados

Pregunta típica:

```text
¿Cuáles son los kardex que tienen número de instrumento?
```

Pensamiento:

- kardex visible = `P_TICK.NU_KARD`
- instrumento = `P_TRAM.NU_INST`
- fecha instrumento = `P_TRAM.FE_ESCR_TRAM`

Base:

```sql
FROM R_TICK_SERV RTS
JOIN P_TICK PT ON PT.CO_TICK_CONT = RTS.CO_TICK_CONT
JOIN P_TRAM TR ON TR.CO_TICK_SERV = RTS.CO_TICK_SERV
WHERE TR.NU_INST IS NOT NULL
```

---

## Patrón 3 — Producción por usuario responsable

Pregunta típica:

```text
¿Cuántas escrituras hizo PROCESOS?
```

Pensamiento:

- usuario responsable:
  1. `CO_USUA_ABOG`
  2. fallback `CO_USUA_MODI`
- si te dan un login como `PROCESOS`, revisar primero `P_USUA.ID_USUA`

Base:

```sql
LEFT JOIN P_USUA U
  ON U.CO_USUA = COALESCE(NULLIF(PT.CO_USUA_ABOG, 0), PT.CO_USUA_MODI)
```

Filtro sugerido:

```sql
U.ID_USUA = ?
```

---

## Patrón 4 — Cliente

Pregunta típica:

```text
¿Quién es el cliente?
```

Resolver así:

- fuente principal: `P_CLIE`
- complementar si hace falta con:
  - `H_CLIE_NATU`
  - `H_CLIE_MAIL`

Base:

```sql
JOIN P_CLIE CL ON CL.CO_CLIE = PT.CO_CLIE
```

---

## Patrón 5 — Agrupar por servicio exacto

Pregunta típica:

```text
¿Cuánto ingresó el servicio TRANSFERENCIA VEHICULAR?
```

Pensamiento:

- usar `P_TRAM.CO_SERV`
- si conoces el código exacto, filtrar por `CO_SERV`

Base:

```sql
WHERE TR.CO_SERV = ?
```

---

## Patrón 6 — Agrupar por familia notarial

Pregunta típica:

```text
¿Cuánto se hizo en vehiculares?
```

Pensamiento:

- puede que no sea un único `CO_SERV`
- usar `P_SERV.CO_REGI_NOTA`
- para vehiculares Legal, revisar `CO_REGI_NOTA = 2`

Base:

```sql
JOIN P_SERV PS ON PS.CO_SERV = TR.CO_SERV
WHERE PS.CO_REGI_NOTA = ?
```

---

## Patrón 7 — Participantes de un trámite

Pregunta típica:

```text
¿Qué participantes tiene este trámite?
```

Base:

```sql
FROM R_PRTC_TRAM RPT
JOIN P_PRTC P ON P.CUP = RPT.CUP
LEFT JOIN H_PRTC_NATU N ON N.CUP = P.CUP
LEFT JOIN H_PRTC_JURI J ON J.CUP = P.CUP
LEFT JOIN A_TIPO_PRTC ATP ON ATP.CO_TIPO_PRTC = RPT.CO_TIPO_PRTC
WHERE RPT.CO_TICK_SERV = ?
```

---

## Patrón 8 — Búsqueda de participante en Legal

Pregunta típica:

```text
Quiero recuperar el último participante correcto por DNI para Legal
```

Pensamiento:

1. priorizar último uso en Legal
2. si no existe, último uso en Operaciones
3. si no existe, cliente (`P_CLIE` / `H_CLIE_NATU` / `H_CLIE_MAIL`)
4. si es DNI e incompleto, RENIEC

Base conceptual:

```sql
R_PRTC_TRAM -> P_TRAM
```

Condición funcional:

```sql
P_TRAM.IN_KARD = 1
```

---

## Patrón 9 — Documento guardado o PDF guardado

Pregunta típica:

```text
¿Ese kardex ya tiene Word o PDF?
```

Fuente:

```sql
Z_KARD_ESCR
```

Columnas:

- `IM_DOCU`
- `IM_DOCU_PDF`

No usar:

- etapas del trámite como sustituto

---

## Patrón 10 — Conceptos de liquidación del servicio

Pregunta típica:

```text
¿Qué conceptos tiene configurado este servicio?
```

Base:

```sql
FROM R_SERV_CPTO_TARI R
JOIN P_CPTO C ON C.CO_CPTO = R.CO_CPTO
WHERE R.CO_SERV = ?
  AND R.CO_COMP = ?
```

---

## Patrón 11 — Filtrar por fecha de firma

Pregunta típica:

```text
Quiero los servicios firmados en mayo 2026
```

Pensamiento:

- si la pregunta es por firma, usar `R_TICK_SERV.FE_FIRM_COMP`
- no cambiarlo por fecha de ticket ni por fecha de instrumento

Base:

```sql
FROM R_TICK_SERV RTS
JOIN P_TICK PT ON PT.CO_TICK_CONT = RTS.CO_TICK_CONT
JOIN P_TRAM TR ON TR.CO_TICK_SERV = RTS.CO_TICK_SERV
WHERE RTS.FE_FIRM_COMP >= ?
  AND RTS.FE_FIRM_COMP < ?
```

---

## Patrón 12 — Participantes casados de un kardex

Pregunta típica:

```text
Quiero saber los participantes casados de tal kardex
```

Pensamiento:

- ubicar el trámite desde el kardex
- participante natural en `H_PRTC_NATU`
- casado = `CO_ESTA_CIVI = 2`

Base:

```sql
FROM P_TICK PT
JOIN R_TICK_SERV RTS ON RTS.CO_TICK_CONT = PT.CO_TICK_CONT
JOIN R_PRTC_TRAM RPT ON RPT.CO_TICK_SERV = RTS.CO_TICK_SERV
JOIN H_PRTC_NATU N ON N.CUP = RPT.CUP
WHERE PT.NU_KARD = ?
  AND N.CO_ESTA_CIVI = 2
```

---

## Patrón 13 — Participantes con DNI

Pregunta típica:

```text
Quiero todos los participantes que tengan DNI
```

Pensamiento:

- DNI = `A_TDOC_IDEN.CO_TDOC_IDEN = 1`

Base:

```sql
FROM H_PRTC_NATU N
WHERE N.CO_TDOC_IDEN = 1
```

---

## Patrón 14 — Extranjeros ingresados en un rango

Pregunta típica:

```text
Dame todos los extranjeros ingresados en mayo 2026
```

Pensamiento:

- “extranjeros” normalmente:
  - pasaporte = `3`
  - carnet de extranjería = `4`
- si la consulta habla de “ingresados”, primero aclarar qué fecha usar
- si se refiere al alta del participante en el sistema, validar columna/tabla del alta antes del SQL final

Base documental mínima:

```sql
WHERE N.CO_TDOC_IDEN IN (3, 4)
```

---

## Patrón 15 — Recibos pagados de una fecha

Pregunta típica:

```text
Necesito todos los recibos pagados de tal fecha
```

Pensamiento:

- recibo = `A_TDOC.CO_TDOC = 7`
- pagado normal = `P_CABE_CAJA.IN_ESTA_CAJA = 6`
- fecha de caja = `P_CABE_CAJA.FE_CABE_CAJA`

Base:

```sql
FROM P_CABE_CAJA PC
JOIN A_SEMI_TDOC ST ON ST.CO_SEMI_TDOC = PC.CO_SEMI_TDOC
JOIN A_TDOC TD ON TD.CO_TDOC = ST.CO_TDOC
WHERE TD.CO_TDOC = 7
  AND PC.IN_ESTA_CAJA = 6
  AND PC.FE_CABE_CAJA >= ?
  AND PC.FE_CABE_CAJA < ?
```

---

## Patrón 16 — Facturados y cobranza

Pregunta típica:

```text
Quiero mezclar cancelados y solo facturados
```

Pensamiento:

- `cancelado` normal:
  - `P_CABE_CAJA.IN_ESTA_CAJA = 6`
  - fecha = `FE_CABE_CAJA`
- `facturado` al crédito:
  - `P_CABE_CAJA.IN_ESTA_CAJA = 5`
  - fecha = `FE_CABE_CAJA`
- si además se quiere ver cobro posterior de esos créditos:
  - usar `R_CAJA_PAGO -> P_PAGO_DOCU -> P_CABE_CAJA`
  - fecha = `P_PAGO_DOCU.FE_PAGO_DOCU`

Base de cobranza:

```sql
FROM R_CAJA_PAGO RP
JOIN P_PAGO_DOCU PD ON PD.CO_PAGO_DOCU = RP.CO_PAGO_DOCU
JOIN P_CABE_CAJA PC ON PC.CO_CABE_CAJA = RP.CO_CABE_CAJA
```

Orden:

```sql
ORDER BY R.NU_ORDE
```

---

## Patrón 11 — Conceptos libres o subconceptos

Pregunta típica:

```text
¿Qué subconcepto o texto libre terminó en la liquidación?
```

Fuente:

```sql
H_PRES_TICK.DE_DETA_CPTO
```

Si el análisis es por servicio:

- puede complementar con `CO_CPTO`
- y si aplica, con `H_SUB_SERV.CO_CPTO`

---

## Patrón 12 — Dinámicos de escritura

Pregunta típica:

```text
¿Qué campos usa la escritura / parte / acta?
```

Resolver así:

1. servicio
2. `P_SERV.CO_REGI_NOTA`
3. `A_DOCU_FIRM`
4. `H_CODO`

Base:

```sql
FROM H_CODO HC
JOIN A_TIPO_CAMP_type TC ON TC.CO_TIPO_CAMP = HC.CO_TIPO_CAMP
WHERE HC.CO_DOCU_FIRM = ?
ORDER BY HC.NU_ORDE
```

---

## Patrón 13 — Medio de pago leído por IA

Pregunta típica:

```text
¿Qué registros vienen de IA?
```

Fuente:

```sql
H_JSON_TRAM
```

Interpretación:

- `CO_TIPO_API = 1` → minuta IA
- `CO_TIPO_API = 2` → medio de pago

Si es pago exhibible:

- revisar `H_DL939_PAGO.IN_EXHI = 1`

---

## Regla de oro para el bot

Si la pregunta menciona:

- un grupo notarial amplio → pensar en `CO_REGI_NOTA`
- un servicio puntual → pensar en `CO_SERV`
- un dato visible del ticket → pensar en `P_TICK`
- un dato del trámite → pensar en `P_TRAM`
- participantes → pensar en `R_PRTC_TRAM`
- cliente → pensar en `P_CLIE` y, si hace falta más detalle, `H_CLIE_NATU` / `H_CLIE_MAIL`
- documento generado → pensar en `Z_KARD_ESCR`
- liquidación → pensar en `H_PRES_TICK` + `R_SERV_CPTO_TARI`
