import os
os.environ["HF_HUB_OFFLINE"] = "1"
# anula la consulta constante de diferencias de repo con el actual.

from laya import Router
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-3s| %(asctime)s| %(name)s| %(funcName)s: %(lineno)d   %(message)s"
)

log= logging.getLogger("Laya testing")

router = Router()

Urgency_labels= [
    "not urgent", 
    "soon", 
    "blocking"
]

state = "Hola, sabe que me cobraron 2 veces, me gustaria que lo solucionen"
questions = {
    "department": {
        "type": "choice", 
        "instructions": "Which department should handle this?",
        "criteria": {
            "billing": "invoices, payments, refunds",
            "technical": "bugs, outages, system errors",
            "other": "everything else"
        }
    },
    "urgency": {
        "type": "score", 
        "instructions": "How urgent is this?",
        "criteria": Urgency_labels
    },
    "churn_risk": {
        "type": "noul",
        "instructions": "Does the user threaten to cancel or leave?"
    },
}




result = router.predict(state, questions)
for k,v in result.items():
    print(f"{str(k):>20}{v}\n")

score_response= result["answers"]["urgency"]["score"]


log.info(f'choice [] {result["answers"]["department"]["choice"]}')
log.info(f'churn risk [noul] {result["answers"]["churn_risk"]["noul"]}')
log.info(f'model {result["routing"]["model"]}')
log.info(f'urgency: {Urgency_labels[min(round(score_response), len(Urgency_labels)-1)]}')