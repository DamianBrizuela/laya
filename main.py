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
result = router.predict("I was charged twice.", questions)

log.info(f"raw result: \n\t{result}")
log.info(f'\t{result["answers"]["queue"]["choice"]}')