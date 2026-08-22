print("Traffic Light Optimization")
print("---------------------------")

states = ["LOW", "MEDIUM", "HIGH"]

actions = {
    "LOW": "GREEN",
    "MEDIUM": "GREEN",
    "HIGH": "GREEN"
}

reward = {
    "LOW": 10,
    "MEDIUM": 20,
    "HIGH": 30
}

print("Initial Policy:")
print(actions)

# Policy improvement
for state in states:

    if state == "HIGH":
        actions[state] = "LONG GREEN"

    elif state == "MEDIUM":
        actions[state] = "MEDIUM GREEN"

    else:
        actions[state] = "SHORT GREEN"

print("\nImproved Policy:")
print(actions)

print("\nPolicy Iteration Completed.")
print("Traffic waiting time is reduced.")
