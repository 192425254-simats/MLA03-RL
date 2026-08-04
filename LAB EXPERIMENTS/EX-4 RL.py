# Experiment 4
# Bellman Equation for an Autonomous Delivery Robot

# States
states = ["Warehouse", "Road1", "Road2", "Customer"]

# Actions
actions = {
    "Warehouse": ["Go"],
    "Road1": ["Forward", "Turn"],
    "Road2": ["Forward"],
    "Customer": []
}

# Transition probabilities
transitions = {
    ("Warehouse", "Go"): ("Road1", 1.0),
    ("Road1", "Forward"): ("Customer", 1.0),
    ("Road1", "Turn"): ("Road2", 1.0),
    ("Road2", "Forward"): ("Customer", 1.0)
}

# Rewards (Higher reward = Lower travel cost)
rewards = {
    "Warehouse": 0,
    "Road1": -5,
    "Road2": -10,
    "Customer": 100
}

# Discount factor
gamma = 0.9

# Initialize state values
V = {}

for state in states:
    V[state] = 0

V["Customer"] = 100

# Bellman Value Iteration
for i in range(10):

    new_V = V.copy()

    for state in states:

        if state == "Customer":
            continue

        values = []

        for action in actions[state]:

            next_state, probability = transitions[(state, action)]

            value = rewards[next_state] + gamma * probability * V[next_state]

            values.append(value)

        new_V[state] = max(values)

    V = new_V

# Display state values
print("State Values")
print("----------------------")

for state in states:
    print(state, ":", round(V[state], 2))

# Find optimal policy
print("\nOptimal Policy")
print("----------------------")

for state in states:

    if state == "Customer":
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
