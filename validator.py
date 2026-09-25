import numpy as np
from dataclasses import dataclass

@dataclass
class ValidationResult:
    is_valid: bool
    reason: str

def validate_audio(audio) -> ValidationResult:
    if audio is None:
        return ValidationResult(False, "Audio input is None")

    if not isinstance(audio, np.ndarray):
        return ValidationResult(False, "Input is not a NumPy array")

    if audio.size == 0:
        return ValidationResult(False, "Audio input is empty")

    if np.isnan(audio).any():
        return ValidationResult(False, "Audio contains NaN values")

    if np.isinf(audio).any():
        return ValidationResult(False, "Audio contains Infinite values")

    return ValidationResult(True, "Validation Passed")