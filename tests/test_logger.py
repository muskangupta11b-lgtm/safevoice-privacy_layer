from logger import log_event
from config import VALIDATION_PASS,VALIDATION_FAIL,DECISION_ALLOW,DECISION_BLOCK
log_event(
    validation_result=VALIDATION_PASS,
    decision=DECISION_ALLOW,
    reason="Validation Passed"
)

log_event(
    validation_result=VALIDATION_FAIL,
    decision=DECISION_BLOCK,
    reason="Audio input is empty"
)

log_event(
    validation_result=DECISION_BLOCK,
    decision=DECISION_BLOCK,
    reason="Audio contains NaN values"
)
print("Logs written successfully!")