# import numpy as np
# from logger import log_event
# from validator import validate_audio, ValidationResult
# from network import NetworkMonitor, NetworkResult
# from dataclasses import dataclass
# from validator import validate_audio
# from network import NetworkMonitor
# from policy import evaluate_policy

# @dataclass
# class PrivacyResult:
#     audio: np.ndarray
#     decision: str
#     reason: str
#     validation: ValidationResult
#     network: NetworkResult

# def run_privacy_framework(audio):
#     monitor = NetworkMonitor() 
#     monitor.start()
#     # 2. Validate audio
#     validation = validate_audio(audio)

#     # 3. Stop monitoring and get result

    
#     network = monitor.stop()
# # 4. Evaluate privacy policy
#     policy = evaluate_policy(
#         validation.is_valid,
#         network.is_local,
#         True # logger is available
#     )

#     # 5. Log the event
#     log_event(validation_result = (
#     "PASS" if validation.is_valid else "FAIL"),
#     decision=policy.decision,
#     reason=policy.reason
#     )

#     # 6. Return result
#     return PrivacyResult(
#     audio=audio,
#     decision=policy.decision,
#     reason=policy.reason,
#     validation=validation,
#     network=network
# )







import numpy as np
from dataclasses import dataclass

from logger import log_event
from validator import validate_audio, ValidationResult
from network import NetworkMonitor, NetworkResult
from policy import evaluate_policy


@dataclass
class PrivacyResult:
    audio: np.ndarray
    decision: str
    reason: str
    validation: ValidationResult
    network: NetworkResult


def run_privacy_framework(audio):

    monitor = NetworkMonitor()

    # 1. Start network monitoring
    monitor.start()

    # 2. Validate audio
    validation = validate_audio(audio)

    # 3. Stop monitoring
    network = monitor.stop()

    # 4. Evaluate privacy policy
    policy = evaluate_policy(
    validation.is_valid,
    network.is_local
)

    try:
        log_event(
        validation_result=("PASS" if validation.is_valid else "FAIL"),
        decision=policy.decision,
        reason=policy.reason
    )
    except Exception:
        print("Warning: Privacy event could not be logged.")
    # 6. Return complete result
    return PrivacyResult(
        audio=audio,
        decision=policy.decision,
        reason=policy.reason,
        validation=validation,
        network=network
    )