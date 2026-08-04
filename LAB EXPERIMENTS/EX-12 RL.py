import random

# States
states = ["Object", "Picked", "Placed"]

# Actions
actions = ["Pick", "Place"]

# Rewards
rewards = {
    ("Object", "Pick"): 20,
    ("Picked", "Place"): 100
}

# Policy Table
policy = {}

for state in states:
    policy[state] = {}
    for action in actions:
        policy[state][action] = 0.5

# Learning parameters
alpha = 0.1
episodes = 100

# Training
for episode in range(episodes):

    state = "Object"

    while state != "Placed":

        # Select action based on policy
        if random.random() < policy[state]["Pick"]:
            action = "Pick"
        else:
            action = "Place"

        # Environment
        if state == "Object" and action == "Pick":
            reward = rewards[(state, action)]
            next_state = "Picked"

        elif state == "Picked" and action == "Place":
            reward = rewards[(state, action)]
            next_state = "Placed"

        else:
            reward = -10
            next_state = state

        # Policy Update
        if reward > 0:
            policy[state][action] += alpha * (1 - policy[state][action])
        else:
            policy[state][action] -= alpha * policy[state][action]

        state = next_state

# Display Learned Policy
print("Learned Policy")
print("------------------------")

for state in states:
    print(state, ":", policy[state])

# Test Robot
print("\nRobot Pick-and-Place")
print("------------------------")

state = "Object"
print(state)

while state != "Placed":

    action = max(policy[state], key=policy[state].get)

    print("Action :", action)

    if state == "Object":
        state = "Picked"

    elif state == "Picked":
        state = "Placed"

    print("Next State :", state)

print("\nTask Completed Successfully!")
