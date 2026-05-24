# Reglas de Negocio de Legasys Web

## Regla: Trámites Escriturados (Legal y Kardex)
Para saber si un Kardex (trámite) está "Escriturado":
- NO basta con buscar en P_TRAM.
- Un trámite está escriturado SOLAMENTE si tiene un número de instrumento (`NU_INST IS NOT NULL`) Y además tiene una fecha de escritura registrada (`FE_ESCR_TRAM IS NOT NULL`).

## Regla: Trámites Concluidos (Legal)
Para saber si un trámite está "Concluido":
- Se debe revisar la tabla de relación de tickets de servicio `R_TICK_SERV`.
- Un trámite está concluido SOLAMENTE si tiene fecha de firma de conclusión (`FE_FIRM_COMP IS NOT NULL`).

## Regla: Ingresos de Caja y Finanzas Netas
Para calcular cuánto dinero ingresó a la notaría (montos netos, subtotales o totales cobrados):
1. Los ingresos positivos provienen de cajas facturadas o pagadas (`P_CABE_CAJA.IN_ESTA_CAJA IN (6, 12)`), y que NO estén anuladas (`P_CABE_CAJA.IN_ESTA NOT IN (0, 2)`).
2. Documentos que SUMAN ingresos: Boletas (A_TDOC.CO_TDOC = 17) y Facturas (A_TDOC.CO_TDOC = 16).
3. Documentos que RESTAN ingresos: Notas de Crédito (A_TDOC.CO_TDOC = 18 o 19). Estas notas están en `P_CABE_NOTA` y su detalle en `H_DETA_NOTA` (`MO_TOTA_NC`).
4. Al cruzar `H_DETA_CAJA` (lo que ingresó por cada concepto) y `H_DETA_NOTA` (lo que se devolvió por concepto), el ingreso real es: `H_DETA_CAJA.MO_TOTA - COALESCE(H_DETA_NOTA.MO_TOTA_NC, 0)`.

## Regla: Presupuestos y Pendientes (Saldos de Trámites)
Para saber cuánto debe un cliente por un Kardex o Ticket:
- El presupuesto inicial vive en `H_PRES_TICK.MO_PRES_NOTA` o sumando sus detalles.
- El saldo pendiente (deuda real que el cliente aún no paga) está en la tabla de caja principal: `P_CABE_CAJA.MO_DEUD_PAGO`. Todo lo que tenga `MO_DEUD_PAGO > 0` significa que aún le falta pagar.

## Regla: Situación Registral en RRPP (Registros Públicos)
Un trámite o kardex pasa por varios estados en RRPP. Se identifica usando `P_TRAM.CO_SITU_TRAM`:
- "Ingreso a RRPP": `CO_SITU_TRAM = 1`.
- "Observado": `CO_SITU_TRAM IN (2, 17)`.
- "Inscrito" o terminado en registro: `CO_SITU_TRAM = 5`.
