# SQL_SOURCE_OF_TRUTH.md — Fuente oficial por dato funcional

Fecha de corte: 2026-05-21  
Proyecto: Legasys Web

## Objetivo

Este archivo le dice al bot qué tabla y qué columna debe priorizar para responder preguntas funcionales.

`DATABASE_DOCUMENTATION` explica la estructura física.

`SQL_TABLE_RULES.md` explica reglas y joins.

Este archivo responde otra pregunta:

```text
Si me preguntan por X, ¿de dónde debo sacar X primero?
```

## Regla general

Cuando un mismo dato puede salir de varias tablas:

1. usar la fuente funcional oficial
2. si no existe, usar el fallback documentado
3. no inventar una tercera fuente

## Regla general de fechas

Si el usuario hace una consulta con tiempo, el bot debe validar dos cosas antes de responder:

1. qué fecha quiere usar realmente
2. si hace falta un rango y no lo dio, pedirlo

Fechas funcionales más comunes:

- fecha de creación del ticket / kardex → `P_TICK.FE_CREA_TICK`
- fecha de instrumento / escritura → `P_TRAM.FE_ESCR_TRAM`
- fecha de firma → `R_TICK_SERV.FE_FIRM_COMP`
- fecha de caja / cobro → tabla de caja correspondiente del flujo consultado

---

## Ticket, trámite y servicio

### Kardex visible

- fuente principal: `P_TICK.NU_KARD`
- no usar como equivalente:
  - `P_TRAM.NU_TRAM`

### Fecha de kardex / fecha de creación del ticket

- fuente principal: `P_TICK.FE_CREA_TICK`
- no usar:
  - `TS_USUA_MODI`

### Fecha de firma

- fuente principal: `R_TICK_SERV.FE_FIRM_COMP`
- usarla cuando la pregunta diga:
  - “fecha de firma”
  - “firmados en un rango”
  - “servicios/trámites firmados”
- no reemplazarla por:
  - `P_TICK.FE_CREA_TICK`
  - `P_TRAM.FE_ESCR_TRAM`

### Módulo del ticket

- fuente principal: `P_TICK.CO_MODU`
- valores funcionales conocidos:
  - `1` = Legal
  - `2` = Operaciones

### Módulo del servicio

- fuente principal: `P_SERV.CO_MODU`
- este campo también existe y es útil como apoyo funcional cuando se consulta catálogo de servicios
- aun si `DATABASE_DOCUMENTATION` ya enumera columnas, el bot debe recordar que `P_SERV.CO_MODU` existe porque ayuda a filtrar servicios por módulo sin pasar todavía por tickets

### Servicio principal del trámite

- fuente principal: `P_TRAM.CO_SERV`

### Registro notarial / familia del servicio

- fuente principal: `P_SERV.CO_REGI_NOTA`
- resolver contra:
  - `A_REGI_NOTA.CO_REGI_NOTA`

### Número de instrumento

- fuente principal: `P_TRAM.NU_INST`

### Número de control

- fuente principal: `P_TRAM.NU_CTRL`

### Fecha de instrumento / fecha de escritura

- fuente principal por defecto: `P_TRAM.FE_ESCR_TRAM`
- advertencia:
  - en algunos flujos documentales la fecha funcional visible puede depender de dinámicos (`H_CODO` / `R_CODO_KARD`)
  - si la pregunta es “fecha guardada del instrumento” usar `P_TRAM.FE_ESCR_TRAM`
  - si la pregunta es “fecha mostrada en el documento dinámico”, validar si depende del campo documental

### Etapa actual del trámite

- fuente principal: `P_TRAM.CO_ETAP_TRAM`
- nombre de etapa:
  - `A_ETAP_TRAM_type`

---

## Cliente y participantes

### Cliente del ticket

- fuente principal: `P_TICK.CO_CLIE -> P_CLIE.CO_CLIE`
- nombre visible frecuente:
  - `P_CLIE.NO_BUSQ`
- datos complementarios del cliente:
  - `H_CLIE_NATU`
  - `H_CLIE_MAIL`

### Cliente funcional del sistema

- fuente principal: `P_CLIE`
- detalle natural complementario:
  - `H_CLIE_NATU`
- correos complementarios:
  - `H_CLIE_MAIL`

### Regla importante

- no usar `R_PRTC_TRAM.IN_CLIE` como fuente de cliente
- aunque esa bandera exista, hoy no debe considerarse la fuente oficial del cliente

### Participante prioritario en búsquedas de Legal

- fuente principal:
  - último participante usado en trámites Legal
- resolución:
  - `R_PRTC_TRAM.CO_TICK_SERV -> P_TRAM.CO_TICK_SERV`
  - priorizar `P_TRAM.IN_KARD = 1`
- fallback:
  - último uso en Operaciones (`IN_KARD = 0` o `NULL`)
  - luego cliente por `P_CLIE` / `H_CLIE_NATU` / `H_CLIE_MAIL`
  - luego RENIEC para DNI si falta

### Dirección de participante en Legal

- fuente principal funcional:
  - última dirección útil de `H_PRTC_DIRE`
- no depender solo de:
  - `P_PRTC.NS_ULTI_DIRE`

### Estado civil del participante natural

- fuente principal: `H_PRTC_NATU.CO_ESTA_CIVI`
- resolver catálogo con:
  - `A_ESTA_CIVI.CO_ESTA_CIVI`

### Sexo / género del participante natural

- fuente principal: `H_PRTC_NATU.CO_INDI_GENE`
- si es DNI y el registro local está incompleto:
  - RENIEC puede completar

### Fecha de nacimiento del participante natural

- fuente principal: `H_PRTC_NATU.FE_NACI_UIF`
- si es DNI y falta:
  - RENIEC puede completar

### Documento del participante natural

- fuente principal:
  - `H_PRTC_NATU.CO_TDOC_IDEN`
  - `H_PRTC_NATU.NU_DOCU_IDEN`
- resolver catálogo con:
  - `A_TDOC_IDEN.CO_TDOC_IDEN`

### Razón social del participante jurídico

- fuente principal: `H_PRTC_JURI.NO_RAZO_SOCI`

---

## Usuarios

### Usuario responsable del ticket

Prioridad:

1. `P_TICK.CO_USUA_ABOG`
2. si está vacío o `0`, `P_TICK.CO_USUA_MODI`

### Login o identificador del usuario

- fuente frecuente: `P_USUA.ID_USUA`
- no asumir que el identificador visible es siempre `NO_USUA`

### Nombre visible del usuario

- fuente frecuente: `P_USUA.NO_USUA`

---

## Liquidación, conceptos y caja

### Conceptos disponibles para un servicio

- fuente principal: `R_SERV_CPTO_TARI`
- siempre filtrar por:
  - `CO_SERV`
  - `CO_COMP`
  - y cuando aplique, `CO_TARI`

### Orden visual de conceptos

- fuente principal: `R_SERV_CPTO_TARI.NU_ORDE`

### Monto base de concepto/tarifa

- fuente principal: `R_SERV_CPTO_TARI.IM_TARI`

### Texto visible del concepto/subconcepto en liquidación

- fuente principal: `H_PRES_TICK.DE_DETA_CPTO`

### Servicio visible del detalle de caja

- fuente principal: `H_DETA_CAJA.DE_DETA_CAJA`

### Concepto/subconcepto visible del detalle de caja

- fuente principal: `H_DETA_CAJA.DE_DETA_CPTO`

### Documento de caja / comprobante

- la cabecera depende del flujo de caja
- si la pregunta es por detalle del cobro, normalmente partir desde tablas de caja y no desde el ticket

### Cabecera principal de caja

- fuente principal: `P_CABE_CAJA`
- fecha funcional de caja / cobro directo:
  - `P_CABE_CAJA.FE_CABE_CAJA`

### Estado de caja

- fuente principal:
  - `P_CABE_CAJA.IN_ESTA_CAJA`
- resolver catálogo con:
  - `A_ESTA_CAJA.CO_ESTA_CAJA`

### Comprobante de caja

- fuente principal:
  - `A_SEMI_TDOC.CO_TDOC`
- resolver catálogo con:
  - `A_TDOC.CO_TDOC`

### Facturados al crédito

- fuente principal:
  - `P_CABE_CAJA` con `IN_ESTA_CAJA = 5`
- fecha funcional para ese reporte:
  - `P_CABE_CAJA.FE_CABE_CAJA`
- interpretación:
  - documento facturado / al crédito pendiente de cobranza

### Cancelados / pagados normales

- fuente principal:
  - `P_CABE_CAJA` con `IN_ESTA_CAJA = 6`
- fecha funcional para ese reporte:
  - `P_CABE_CAJA.FE_CABE_CAJA`

### Cobranza de créditos

- base relacional:
  - `R_CAJA_PAGO -> P_PAGO_DOCU -> P_CABE_CAJA`
- fecha funcional para cobranza:
  - `P_PAGO_DOCU.FE_PAGO_DOCU`
- usar esta ruta cuando la pregunta combine facturados pendientes con cobros posteriores por cobranza

### Concepto libre en liquidación

- si no existe en `R_SERV_CPTO_TARI`, debe crearse relación con:
  - monto `0.00`
  - tarifa base del flujo

### Subservicio o subconcepto operativo

- fuente principal: `H_SUB_SERV`
- si se pregunta qué concepto financiero relaciona:
  - usar `H_SUB_SERV.CO_CPTO`

---

## Documentos, escritura y dinámicos

### Documento configurado para un registro

- fuente principal: `A_DOCU_FIRM`
- relación:
  - `A_DOCU_FIRM.CO_REGI_NOTA`
  - `P_SERV.CO_REGI_NOTA`

### Campos dinámicos configurados del documento

- fuente principal: `H_CODO`
- orden:
  - `H_CODO.NU_ORDE`
- tipo:
  - `H_CODO.CO_TIPO_CAMP -> A_TIPO_CAMP_type`

### Valor guardado de un campo dinámico

- fuente principal: `R_CODO_KARD`
- relación:
  - `R_CODO_KARD.CO_CODO -> H_CODO.CO_CODO`

### Documento Word guardado

- fuente principal: `Z_KARD_ESCR.IM_DOCU`

### PDF guardado

- fuente principal: `Z_KARD_ESCR.IM_DOCU_PDF`

### Existencia documental en UI

- si la pregunta es “¿tiene documento?” o “¿tiene pdf?”
- la fuente debe ser `Z_KARD_ESCR`
- no usar como fuente principal etapas de seguimiento

---

## Seguimiento y auditoría

### Etapa actual

- fuente principal: `P_TRAM.CO_ETAP_TRAM`

### Historial de etapas

- fuente principal: `H_SGMT_TRAM`

### Auditoría funcional de cambios sensibles

- fuente principal: `H_SGMT_LOG`

### Autorizado imprimir

- fuente principal funcional: `H_SGMT_TRAM`
- no usar esta marca para inferir existencia de documento/PDF

---

## IA, QR y nube

### Proceso IA / resultado IA del trámite

- fuente principal: `H_JSON_TRAM`

### Tipo de integración IA

- fuente principal: `H_JSON_TRAM.CO_TIPO_API`
- valores conocidos:
  - `1` = Minuta IA
  - `2` = Medio de pago

### Documento digital QR

- fuentes principales:
  - `P_DOCU_DIGI_QR`
  - `H_DOCU_DIGI_QR_PRTC`
  - `H_DOCU_DIGI_QR_ESTA`

---

## Reglas cortas para el bot

Si la pregunta menciona:

- `kardex` → pensar primero en `P_TICK.NU_KARD`
- `instrumento` → pensar primero en `P_TRAM.NU_INST`
- `control` → pensar primero en `P_TRAM.NU_CTRL`
- `cliente` → decidir si es cliente del ticket (`P_CLIE`) o cliente del trámite (`R_PRTC_TRAM.IN_CLIE = 1`)
- `cliente` → usar siempre `P_CLIE` y, si hace falta más detalle, `H_CLIE_NATU` y `H_CLIE_MAIL`
- `usuario responsable` → `CO_USUA_ABOG`, si no `CO_USUA_MODI`
- `documento/pdf guardado` → `Z_KARD_ESCR`
- `campo dinámico` → `H_CODO` + `R_CODO_KARD`
- `familia documental` → `P_SERV.CO_REGI_NOTA`
- `módulo del servicio` → `P_SERV.CO_MODU`
- `módulo del ticket` → `P_TICK.CO_MODU`
