 
import numpy as np
from privacy_framework import run_privacy_framework

audio = np.random.rand(44100)

privacy = run_privacy_framework(audio)

print("\n------ Privacy Framework Test ------")
print("Decision        :", privacy.decision)
print("Policy Reason   :", privacy.reason)

print("\nValidation Result")
print("Valid           :", privacy.validation.is_valid)
print("Reason          :", privacy.validation.reason)

print("\nNetwork Result")
print("Local           :", privacy.network.is_local)
print("Bytes Before    :", privacy.network.bytes_before)
print("Bytes After     :", privacy.network.bytes_after)
print("Bytes Sent      :", privacy.network.bytes_sent)