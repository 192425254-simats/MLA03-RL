import random

# States
states = ["Start", "Path", "Obstacle", "Goal"]

# Actions
actions = ["Move"]

# Rewards
rewards = {
    "Start": 0,
    "Path": 10,
    "Obstacle": -20,
    "Goal": 100
}

# State transitions
transitions = {
    "Start": "Path",
    "Path": "Goal",
    "Obstacle": "Path",
    "Goal": "Goal"
}

# Parameters
alpha = 0.5
gamma = 0.9
episodes = 100

# Initialize value function (TD)
V = {}
for state in states:
    V[state] = 0

# Initialize Q-table
Q = {}
for state in states:
    Q[state] = {}
    for action in actions:
        Q[state][action] = 0

# ---------------- TD(0) ----------------
for episode in range(episodes):

    state = "Start"

    while state != "Goal":

        action = "Move"
        next_state = transitions[state]
        reward = rewards[next_state]

        V[state] = V[state] + alpha * (
            reward + gamma * V[next_state] - V[state]
        )

        state = next_state

# ---------------- SARSA ----------------
for episode in range(episodes):

    state = "Start"
    action = "Move"

    while state != "Goal":

        next_state = transitions[state]
        reward = rewards[next_state]

        next_action = "Move"

        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * Q[next_state][next_action] - Q[state][action]
        )

        state = next_state
        action = next_action

# ---------------- Q-Learning ----------------
for episode in range(episodes):

    state = "Start"

    while state != "Goal":

        action = "Move"

        next_state = transitions[state]
        reward = rewards[next_state]

        best_next = max(Q[next_state].values())

        Q[state][action] = Q[state][action] + alpha * (
            reward + gamma * best_next - Q[state][action]
        )

        state = next_state

# Display Results
print("TD(0) State Values")
print("-----------------------")
for state in states:
    print(state, ":", round(V[state], 2))

print("\nQ-Table (SARSA & Q-Learning)")
print("-----------------------")
for state in states:
    print(state, ":", Q[state])

print("\nOptimal Robot Path")
print("-----------------------")
print("Start --> Path --> Goal")
print("Goal Reached Successfully!")
