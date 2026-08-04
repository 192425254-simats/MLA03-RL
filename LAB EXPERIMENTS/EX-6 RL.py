import random

# Grid size
rows = 4
cols = 4

# Start and Goal
start = (0, 0)
goal = (3, 3)

# Actions
actions = ["Up", "Down", "Left", "Right"]

# Q-Table
Q = {}

for r in range(rows):
    for c in range(cols):
        Q[(r, c)] = {}
        for action in actions:
            Q[(r, c)][action] = 0

# Parameters
alpha = 0.8
gamma = 0.9
epsilon = 0.2
episodes = 500

# Function to move robot
def move(state, action):
    r, c = state

    if action == "Up":
        r = max(0, r - 1)

    elif action == "Down":
        r = min(rows - 1, r + 1)

    elif action == "Left":
        c = max(0, c - 1)

    elif action == "Right":
        c = min(cols - 1, c + 1)

    return (r, c)

# Training
for episode in range(episodes):

    state = start

    while state != goal:

        # ε-Greedy action selection
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = max(Q[state], key=Q[state].get)

        next_state = move(state, action)

        # Reward
        if next_state == goal:
            reward = 100
        else:
            reward = -1

        # Q-Learning update
        old = Q[state][action]
        future = max(Q[next_state].values())

        Q[state][action] = old + alpha * (reward + gamma * future - old)

        state = next_state

# Testing
print("Optimal Robot Path")
print("---------------------")

state = start
print(state, end="")

while state != goal:

    action = max(Q[state], key=Q[state].get)

    state = move(state, action)

    print(" ->", state, end="")

print("\n\nGoal Reached!")

# Display Q-values
print("\nQ-Values")
print("---------------------")

for state in Q:
    print(state, Q[state])
