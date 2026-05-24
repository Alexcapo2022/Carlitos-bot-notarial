# SQL_FLAGS_AND_STATUS.md — Banderas, códigos y estados funcionales

Fecha de corte: 2026-05-21  
Proyecto: Legasys Web

## Objetivo

Este archivo explica el significado funcional de códigos cortos, banderas y columnas que un bot SQL no debe interpretar “a ciegas”.

## Regla general

Una columna tipo:

- `IN_*`
- `CO_*`
- `MO_*`
- `NU_*`

puede parecer autoexplicativa, pero en Legasys muchas tienen significado funcional acordado.

---

## Módulo

## `P_TICK.CO_MODU`

Valores conocidos:

- `1` = Legal (también conocido como "Protocolar")
- `2` = Operaciones (también conocido como "Extraprotocolar")

Uso:

- identificar el módulo del ticket o servicio. Si el usuario pregunta por "protocolar", se refiere a `1`. Si pregunta por "extraprotocolar", se refiere a `2`.

## `P_SERV.CO_MODU`

Uso:

- identificar el módulo del catálogo de servicios
- útil para consultas sobre servicios sin necesidad de pasar por tickets

Regla:

- aunque su detalle físico está en `DATABASE_DOCUMENTATION`, debe recordarse también aquí porque cambia cómo el bot filtra catálogos

---

## Trámite Legal vs Operaciones

## `P_TRAM.IN_KARD`

Valores funcionales:

- `1` = Legal / tiene kardex
- `0` o `NULL` = Operaciones / no tiene kardex

Uso:

- priorizar búsquedas de participantes
- distinguir historial de uso por módulo

---

## Estado genérico

## `IN_ESTA`

Regla general:

- `1` = activo
- `0` = inactivo

Advertencia:

- siempre confirmar si el módulo usa exactamente esta convención, pero en gran parte del sistema sí

Se usa frecuentemente en:

- `A_DOCU_FIRM`
- `H_CODO`
- `R_PRTC_SERV`
- `R_PRTC_TRAM`
- `R_SERV_CPTO_TARI`
- `A_COMP`
- **`R_TICK_SERV` (¡OBLIGATORIO SIEMPRE USAR `IN_ESTA = 1` AQUÍ!)**
- muchas tablas de catálogo y relación

---

## Participantes

## `A_ESTA_CIVI.CO_ESTA_CIVI`

Valores conocidos:

- `1` = soltero
- `2` = casado
- `3` = viudo
- `4` = divorciado
- `5` = conviviente

Uso:

- interpretar `H_PRTC_NATU.CO_ESTA_CIVI`
- consultas como “participantes casados” deben usar `CO_ESTA_CIVI = 2`

## `A_TDOC_IDEN.CO_TDOC_IDEN`

Valores activos conocidos:

- `1` = DNI
- `3` = pasaporte
- `4` = carnet de extranjería
- `8` = RUC
- `12` = sin documento

Uso:

- interpretar `H_PRTC_NATU.CO_TDOC_IDEN`
- consultas como “todos los participantes que tengan DNI” deben usar `CO_TDOC_IDEN = 1`
- consultas como “extranjeros” normalmente deben evaluar:
  - `CO_TDOC_IDEN = 3` (pasaporte)
  - `CO_TDOC_IDEN = 4` (carnet de extranjería)

## `R_PRTC_TRAM.IN_CLIE`

Significado histórico:

- puede marcar un participante como cliente dentro del trámite

Regla actual:

- no usar esta bandera como fuente oficial para obtener el cliente
- para cliente, usar:
  - `P_CLIE`
  - `H_CLIE_NATU`
  - `H_CLIE_MAIL`

## `R_REGI_NOTA.IN_INGR_PRTC`

Valores funcionales conocidos:

- `5` = formulario mixto / genérico

Regla:

- en Operaciones, esta bandera debe resolverse primero por notaría desde `R_REGI_NOTA`

---

## Caja y control financiero

## `A_TDOC.CO_TDOC`

Valores activos conocidos:

- `7` = recibo
- `16` = factura electrónica
- `17` = boleta electrónica

Uso:

- interpretar tipos documentarios de caja/facturación
- consultas como “recibos pagados” deben usar `CO_TDOC = 7`

## `A_COMP.IN_SEGU_CAJA`

Valores funcionales:

- `0` o `NULL` = no aplica
- `1` = Legal
- `2` = Operaciones
- `3` = ambos

Uso:

- decidir si se bloquea la generación de borrador por saldo pendiente

## `H_DL939_PAGO.IN_EXHI`

Significado:

- marca exposición/uso del pago en ciertos flujos asistidos o vinculados

Regla:

- en integración IA de medios de pago, se usa `IN_EXHI = 1`

---

## Documento y firma

## `A_ESTA_CAJA.CO_ESTA_CAJA`

Valores conocidos:

- `1` = activo
- `2` = pre-anulado
- `3` = anulado
- `4` = sin facturar
- `5` = facturado
- `6` = cancelado
- `7` = canjeado
- `8` = canjeado/cancelado
- `9` = pendiente
- `10` = anulado/nota de crédito
- `11` = gratuito
- `12` = nota de crédito parcial

Uso:

- `6` es el estado pagado normal más usado en reportes de caja
- `5` representa facturado / al crédito pendiente de cobranza
- cuando la pregunta mezcle pagados y créditos, el bot debe considerar si además hace falta la ruta de cobranza con `P_PAGO_DOCU`

## `R_TICK_SERV.IN_FIRM_COMP`

Significado:

- firma completada

Uso:

- validar si el flujo documental puede seguir ciertos pasos

## `R_TICK_SERV.FE_FIRM_COMP`

Significado:

- fecha de firma / fecha en que el servicio quedó firmado

Uso:

- usar este campo cuando el filtro o la pregunta sea por fecha de firma
- no sustituirlo por `FE_CREA_TICK` ni por `FE_ESCR_TRAM`

## `P_DOCU_DIGI_QR.IN_ESTA_DOCU_DIGI`

Significado:

- estado del documento digital / QR

Regla:

- el significado exacto de cada estado debe tomarse del flujo QR documentado
- no inventar interpretación si la consulta requiere un estado específico

---

## IA

## `H_JSON_TRAM.CO_TIPO_API`

Valores conocidos:

- `1` = Minuta IA
- `2` = Medio de pago

Uso:

- distinguir tipo de integración o lectura asistida

---

## Formularios dinámicos

## `H_CODO.CO_TIPO_CAMP`

Valores conocidos:

- `1` = número
- `2` = letras
- `3` = alfanumérico
- `4` = fecha
- `5` = minuta

Regla:

- no interpretar el valor directamente como texto
- cruzar con `A_TIPO_CAMP_type`

## `H_CODO.IN_TIPO_CAMP`

Regla:

- esta columna se usa funcionalmente junto al tipo documental
- si el query necesita interpretación precisa, revisar el caso de negocio antes de asumir

---

## Registros notariales

## `A_REGI_NOTA.CO_MODU`

Valor conocido:

- `1` = registros notariales de Legal

Regla:

- este campo ayuda a separar familias de registros notariales por módulo

---

## Usuario

## `P_USUA.ID_USUA`

Uso:

- identificador funcional/login del usuario

Regla:

- si la pregunta del usuario usa algo como `PROCESOS`, primero evaluar si se refiere a `ID_USUA`

## `P_USUA.NO_USUA`

Uso:

- nombre visible del usuario

Regla:

- no asumir que el nombre visible es el mismo dato de login

---

## Reglas rápidas para el bot

Si una pregunta usa palabras como:

- `activo` → revisar `IN_ESTA = 1`
- `legal` → revisar `P_TICK.CO_MODU = 1` o `P_TRAM.IN_KARD = 1`
- `operaciones` → revisar `P_TICK.CO_MODU = 2` o `P_TRAM.IN_KARD = 0/null`
- `cliente del trámite` → revisar `R_PRTC_TRAM.IN_CLIE = 1`
- `procesos` u otro login → probar primero `P_USUA.ID_USUA`
