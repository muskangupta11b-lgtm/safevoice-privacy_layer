import numpy as np
from privacy_framework import run_privacy_framework 
audio = np.random.rand(44100)

privacy = run_privacy_framework(audio)
print("Decision:", privacy.decision)
print("Reason:", privacy.reason)
print("Validation:", privacy.validation)
print("Network:", privacy.network)