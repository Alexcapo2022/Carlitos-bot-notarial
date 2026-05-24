from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# Ejemplos de oro ("Golden Queries")
# Aquí definimos las consultas exactas que queremos que el modelo tome como referencia
# cuando el usuario haga preguntas similares. Esto ayuda a que el modelo entienda 
# la lógica de negocio específica de Legasys (ej. uso de CO_COMP, IN_ESTA, etc).

examples = [
    {
        "question": "¿Cuántos trámites o kardex se escrituraron este mes en el registro de Propiedad Inmueble (Registro 1)?",
        "query": "SELECT COUNT(DISTINCT PTICK.NU_KARD) FROM P_TICK PTICK JOIN R_TICK_SERV RTS ON RTS.CO_TICK_CONT = PTICK.CO_TICK_CONT JOIN P_TRAM PT ON PT.CO_TICK_SERV = RTS.CO_TICK_SERV JOIN P_SERV PS ON PS.CO_SERV = PT.CO_SERV WHERE PT.CO_COMP = {co_comp} AND PS.CO_REGI_NOTA = 1 AND PT.NU_INST IS NOT NULL AND PT.FE_ESCR_TRAM IS NOT NULL AND MONTH(PT.FE_ESCR_TRAM) = MONTH(CURDATE()) AND YEAR(PT.FE_ESCR_TRAM) = YEAR(CURDATE());"
    },
    {
        "question": "Dime el monto total cobrado ayer por servicios, descontando las notas de crédito.",
        "query": "SELECT SUM(HDC.MO_TOTA) - COALESCE(SUM(HDN.MO_TOTA_NC), 0) as TOTAL_COBRADO FROM H_DETA_CAJA HDC JOIN P_CABE_CAJA PC ON PC.CO_CABE_CAJA = HDC.CO_CABE_CAJA JOIN A_SEMI_TDOC ST ON ST.CO_SEMI_TDOC = PC.CO_SEMI_TDOC LEFT JOIN P_CABE_NOTA PN ON PN.CO_CABE_CAJA = PC.CO_CABE_CAJA LEFT JOIN H_DETA_NOTA HDN ON HDN.CO_CABE_NOTA = PN.CO_CABE_NOTA AND HDN.CO_DETA_CAJA = HDC.CO_DETA_CAJA WHERE ST.CO_COMP = {co_comp} AND PC.IN_ESTA_CAJA IN (6, 12) AND PC.IN_ESTA NOT IN (0, 2) AND DATE(PC.FE_CABE_CAJA) = CURDATE() - INTERVAL 1 DAY;"
    },
    {
        "question": "Dame la lista de los Kardex de este año que ya tienen fecha de escritura pero que aún tienen un saldo registral o notarial pendiente mayor a cero.",
        "query": "SELECT PT.NU_KARD, PC.MO_DEUD_PAGO FROM P_TRAM PT JOIN R_TICK_SERV RTS ON RTS.CO_TICK_SERV = PT.CO_TICK_SERV JOIN H_PRES_TICK HP ON HP.CO_TICK_SERV = RTS.CO_TICK_SERV JOIN H_DETA_CAJA HDC ON HDC.CO_PRES_TICK = HP.CO_PRES_TICK JOIN P_CABE_CAJA PC ON PC.CO_CABE_CAJA = HDC.CO_CABE_CAJA WHERE PT.CO_COMP = {co_comp} AND YEAR(PT.FE_ESCR_TRAM) = YEAR(CURDATE()) AND PT.FE_ESCR_TRAM IS NOT NULL AND PC.MO_DEUD_PAGO > 0 AND PC.IN_ESTA NOT IN (0, 2);"
    },
    {
        "question": "¿Cuáles son los 5 clientes top por facturación total en caja del mes pasado?",
        "query": "SELECT CL.NO_BUSQ, SUM(PC.MO_NETO) as TOTAL FROM P_CABE_CAJA PC JOIN P_CLIE CL ON CL.CO_CLIE = PC.CO_CLIE JOIN A_SEMI_TDOC ST ON ST.CO_SEMI_TDOC = PC.CO_SEMI_TDOC WHERE ST.CO_COMP = {co_comp} AND PC.IN_ESTA NOT IN (0, 2) AND PC.IN_ESTA_CAJA IN (6, 12) AND MONTH(PC.FE_CABE_CAJA) = MONTH(CURDATE() - INTERVAL 1 MONTH) GROUP BY CL.NO_BUSQ ORDER BY TOTAL DESC LIMIT 5;"
    },
    {
        "question": "Dame los participantes que tiene registrado este kardex V33238",
        "query": "SELECT P.NO_CORT FROM R_PRTC_TRAM RPT JOIN R_TICK_SERV RTS ON RTS.CO_TICK_SERV = RPT.CO_TICK_SERV JOIN P_TRAM PT ON RPT.CO_TICK_SERV = PT.CO_TICK_SERV JOIN P_TICK ON P_TICK.CO_TICK_CONT = RTS.CO_TICK_CONT JOIN P_PRTC P ON RPT.CUP = P.CUP WHERE P_TICK.NU_KARD = 'V33238' AND PT.CO_COMP = {co_comp} AND RPT.IN_ESTA = 1;"
    }
]

# Formato del prompt para cada ejemplo
example_prompt = PromptTemplate(
    input_variables=["question", "query"],
    template="Pregunta del Usuario: {question}\nConsulta SQL Correcta: {query}"
)

# Generamos el string completo con los ejemplos para inyectarlo en el System Prompt
def get_few_shot_examples(co_comp: int) -> str:
    # Formateamos el co_comp en los ejemplos de oro antes de inyectarlos
    formatted_examples = []
    for ex in examples:
        formatted_examples.append(
            example_prompt.format(
                question=ex["question"],
                query=ex["query"].format(co_comp=co_comp)
            )
        )
    return "\n\n".join(formatted_examples)
