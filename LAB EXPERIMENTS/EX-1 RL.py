# Experiment 1 - Medium Level
# Markov Decision Process (MDP) for a Simplified Chess Game

# States
states = ["Start", "Middle", "Check", "Win"]

# Actions
actions = {
    "Start": ["Attack", "Defend"],
    "Middle": ["Attack", "Defend"],
    "Check": ["Checkmate", "Retreat"],
    "Win": []
}

# Transition Model
transitions = {
    ("Start", "Attack"): ("Middle", 0.8),
    ("Start", "Defend"): ("Start", 1.0),

    ("Middle", "Attack"): ("Check", 0.7),
    ("Middle", "Defend"): ("Middle", 1.0),

    ("Check", "Checkmate"): ("Win", 1.0),
    ("Check", "Retreat"): ("Middle", 1.0)
}

# Rewards
rewards = {
    "Start": 0,
    "Middle": 10,
    "Check": 30,
    "Win": 100
}

# Discount factor
gamma = 0.9

# Initialize state values
V = {state: 0 for state in states}
V["Win"] = 100

# Value Iteration
for i in range(10):
    new_V = V.copy()

    for state in states:
        if state == "Win":
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

# Best Policy
print("\nOptimal Policy")
print("----------------------")

for state in states:
    if state == "Win":
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
