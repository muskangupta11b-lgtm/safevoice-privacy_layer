import numpy as np
from dataclasses import dataclass
from config import DECISION_ALLOW,DECISION_BLOCK                        
@dataclass
class PolicyResult:
    decision: str
    reason: str
def evaluate_policy(validation_ok: bool,
                    network_ok: bool,
                    logger_ok: bool) -> PolicyResult:
    if not validation_ok:
        return PolicyResult(
        decision=DECISION_BLOCK,
        reason="PP-01 Failed: Audio validation failed."
        )
    if not network_ok:
        return PolicyResult(
        decision=DECISION_BLOCK,
        reason="PP-02 Failed: Outbound network activity detected."
        )
    if not logger_ok:
        print("Warning: Privacy event could not be logged.")
    return PolicyResult(
    decision=DECISION_ALLOW,
    reason="All privacy policies satisfied."
)