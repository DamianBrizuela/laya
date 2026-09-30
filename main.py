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
questions = {
    "queue": {
        "type": "choice",
        "instructions": "Which team should handle this message?",
        "criteria": {
            "billing": "Charges, invoices, and refunds",
            "technical": "Bugs, errors, and outages",
            "other": "Anything else",
        },
    }
}

result = router.predict("I can´t open de web browser after teh update of my machine.", questions)

log.info(f"raw result: \n\t{result}")
log.info(f'\t{result["answers"]["queue"]["choice"]}')