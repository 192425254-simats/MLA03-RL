# Experiment 7
# Dynamic Programming for Autonomous Taxi Routing

# States
states = ["Start", "Road1", "Road2", "Destination"]

# Actions
actions = {
    "Start": ["Go"],
    "Road1": ["Forward", "Shortcut"],
    "Road2": ["Forward"],
    "Destination": []
}

# Transition probabilities
transitions = {
    ("Start", "Go"): ("Road1", 1.0),
    ("Road1", "Forward"): ("Destination", 1.0),
    ("Road1", "Shortcut"): ("Road2", 1.0),
    ("Road2", "Forward"): ("Destination", 1.0)
}

# Rewards
rewards = {
    "Start": 0,
    "Road1": 20,
    "Road2": 10,
    "Destination": 100
}

# Discount factor
gamma = 0.9

# Initialize state values
V = {}

for state in states:
    V[state] = 0

V["Destination"] = 100

# Value Iteration
for iteration in range(10):

    new_V = V.copy()

    for state in states:

        if state == "Destination":
            continue

        values = []

        for action in actions[state]:

            next_state, probability = transitions[(state, action)]

            value = rewards[next_state] + gamma * probability * V[next_state]

            values.append(value)

        new_V[state] = max(values)

    V = new_V

# Print State Values
print("State Values")
print("-----------------------")

for state in states:
    print(state, ":", round(V[state], 2))

# Find Optimal Policy
print("\nOptimal Taxi Policy")
print("-----------------------")

for state in states:

    if state == "Destination":
        continue

    best_action = None
    best_value = -999

    for action in actions[state]:

        next_state, probability = transitions[(state, action)]

        value = rewards[next_state] + gamma * probability * V[next_state]

        if value > best_value:
            best_value = value
            best_action = action

    print(state, "-->", best_action)
