from policy import evaluate_policy

print("------ Test Case 1 ------")
result = evaluate_policy(
    validation_ok=True,
    network_ok=True,
    logger_ok=True
)
print("Decision :", result.decision)
print("Reason   :", result.reason)


print("\n------ Test Case 2 ------")
result = evaluate_policy(
    validation_ok=False,
    network_ok=True,
    logger_ok=True
)
print("Decision :", result.decision)
print("Reason   :", result.reason)


print("\n------ Test Case 3 ------")
result = evaluate_policy(
    validation_ok=True,
    network_ok=False,
    logger_ok=True
)
print("Decision :", result.decision)
print("Reason   :", result.reason)


print("\n------ Test Case 4 ------")
result = evaluate_policy(
    validation_ok=True,
    network_ok=True,
    logger_ok=False
)
print("Decision :", result.decision)
print("Reason   :", result.reason)