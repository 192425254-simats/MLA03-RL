import random

# Rooms in the smart home
states = ["Living Room", "Kitchen", "Bedroom", "Charging Station"]

# Actions
actions = ["Move"]

# Rewards for reaching each room
rewards = {
    "Living Room": -1,
    "Kitchen": 10,
    "Bedroom": 20,
    "Charging Station": 50
}

# Possible movements
transitions = {
    "Living Room": "Kitchen",
    "Kitchen": "Bedroom",
    "Bedroom": "Charging Station",
    "Charging Station": "Charging Station"
}

# Q-table
Q = {}
for state in states:
    Q[state] = {}
    for action in actions:
        Q[state][action] = 0

# Parameters
learning_rate = 0.8
discount_factor = 0.9
episodes = 100

# Training
for episode in range(episodes):

    state = "Living Room"

    while state != "Charging Station":

        action = "Move"

        next_state = transitions[state]
        reward = rewards[next_state]

        old_q = Q[state][action]

        max_next_q = max(Q[next_state].values())

        new_q = old_q + learning_rate * (
            reward + discount_factor * max_next_q - old_q
        )

        Q[state][action] = new_q

        state = next_state

# Display Q-table
print("Q-Table")
print("---------------------------")

for state in states:
    print(state, ":", Q[state])

# Test the learned path
print("\nRobot Navigation")
print("---------------------------")

state = "Living Room"
total_reward = 0

print(state)

while state != "Charging Station":

    state = transitions[state]
    total_reward += rewards[state]

    print(" -->", state)

print("\nDestination Reached!")
print("Total Reward =", total_reward)
