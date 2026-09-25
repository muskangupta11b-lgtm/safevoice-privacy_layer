import numpy as np
from validator import validate_audio
valid_audio = np.random.rand(44100)
none_audio = None
empty_audio = np.array([])
nan_audio = np.array([1.0, np.nan])
inf_audio = np.array([1.0, np.inf])
test_cases=[("Valid Audio",valid_audio),("None Audio",none_audio),("Empty Audio",empty_audio),("INFINITE AUDIO",inf_audio)]
for test_name,audio in test_cases:
    print(f"\n---{test_cases}---")
    results=validate_audio(valid_audio)
    print(results.is_valid)
    print(results.reason)
