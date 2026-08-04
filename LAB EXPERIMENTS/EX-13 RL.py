import random

# States
states = ["Start", "Near Parking", "Parked"]

# Actions
actions = ["Move", "Park"]

# Rewards
rewards = {
    ("Start", "Move"): 20,
    ("Near Parking", "Park"): 100
}

# Policy probabilities
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

    state = "Start"

    while state != "Parked":

        # Select action based on policy
        if random.random() < policy[state]["Move"]:
            action = "Move"
        else:
            action = "Park"

        # Environment
        if state == "Start" and action == "Move":
            reward = rewards[(state, action)]
            next_state = "Near Parking"

        elif state == "Near Parking" and action == "Park":
            reward = rewards[(state, action)]
            next_state = "Parked"

        else:
            reward = -20
            next_state = state

        # REINFORCE-style policy update
        if reward > 0:
            policy[state][action] += alpha * (1 - policy[state][action])
        else:
            policy[state][action] -= alpha * policy[state][action]

        state = next_state

# Display learned policy
print("Learned Policy")
print("--------------------------")

for state in states:
    print(state, ":", policy[state])

# Test the parking system
print("\nAutonomous Parking")
print("--------------------------")

state = "Start"
print(state)

while state != "Parked":

    action = max(policy[state], key=policy[state].get)

    print("Action :", action)

    if state == "Start":
        state = "Near Parking"

    elif state == "Near Parking":
        state = "Parked"

    print("Next State :", state)

print("\nVehicle Parked Successfully!")
