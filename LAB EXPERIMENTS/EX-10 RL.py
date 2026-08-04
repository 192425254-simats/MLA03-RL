import random

# States
states = ["Start", "Checkpoint", "Delivery"]

# Actions
actions = ["Fly", "Wait"]

# Rewards
rewards = {
    "Start": 0,
    "Checkpoint": 20,
    "Delivery": 100
}

# Battery level
battery = 100

# Q-Table
Q = {}

for state in states:
    Q[state] = {}
    for action in actions:
        Q[state][action] = 0

# Parameters
alpha = 0.8
gamma = 0.9
epsilon = 0.2
episodes = 500

# Training
for episode in range(episodes):

    state = "Start"
    battery = 100

    while state != "Delivery" and battery > 0:

        # ε-Greedy action selection
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        # State transition
        if state == "Start":
            next_state = "Checkpoint"
            battery -= 20

        elif state == "Checkpoint":
            next_state = "Delivery"
            battery -= 30

        else:
            next_state = "Delivery"

        reward = rewards[next_state]

        # Q-Learning update (DQN-inspired)
        old_q = Q[state][action]
        max_next = max(Q[next_state].values())

        Q[state][action] = old_q + alpha * (
            reward + gamma * max_next - old_q
        )

        state = next_state

# Display Q-table
print("Q-Table")
print("-------------------------")

for state in states:
    print(state, ":", Q[state])

# Test Drone Navigation
print("\nOptimal Drone Route")
print("-------------------------")

battery = 100
state = "Start"

print(state)

while state != "Delivery":

    action = max(Q[state], key=Q[state].get)

    if state == "Start":
        battery -= 20
        state = "Checkpoint"

    elif state == "Checkpoint":
        battery -= 30
        state = "Delivery"

    print(" -->", state)

print("\nDelivery Completed Successfully!")
print("Remaining Battery:", battery, "%")
