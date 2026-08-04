# Experiment 3
# Markov Decision Process (MDP) for an Autonomous Warehouse Robot

# States
states = ["Start", "Shelf", "Packing", "Delivery"]

# Actions
actions = {
    "Start": ["Move"],
    "Shelf": ["Pick", "Wait"],
    "Packing": ["Pack"],
    "Delivery": []
}

# Transition Model
transitions = {
    ("Start", "Move"): ("Shelf", 1.0),
    ("Shelf", "Pick"): ("Packing", 0.9),
    ("Shelf", "Wait"): ("Shelf", 1.0),
    ("Packing", "Pack"): ("Delivery", 1.0)
}

# Rewards
rewards = {
    "Start": 0,
    "Shelf": 10,
    "Packing": 30,
    "Delivery": 100
}

# Discount Factor
gamma = 0.9

# Initialize State Values
V = {}
for state in states:
    V[state] = 0

V["Delivery"] = 100

# Value Iteration
for i in range(10):

    new_V = V.copy()

    for state in states:

        if state == "Delivery":
            continue

        values = []

        for action in actions[state]:

            next_state, probability = transitions[(state, action)]

            value = rewards[next_state] + gamma * probability * V[next_state]

            values.append(value)

        new_V[state] = max(values)

    V = new_V

# Display State Values
print("State Values")
print("------------------------")

for state in states:
    print(state, ":", round(V[state], 2))

# Find Optimal Policy
print("\nOptimal Policy")
print("------------------------")

for state in states:

    if state == "Delivery":
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
