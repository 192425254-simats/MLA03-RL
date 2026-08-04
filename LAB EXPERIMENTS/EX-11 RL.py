import random

# Traffic states
states = ["Low Traffic", "Medium Traffic", "High Traffic"]

# Actions
actions = ["Green NS", "Green EW"]

# Reward table
reward_table = {
    "Low Traffic": 10,
    "Medium Traffic": 30,
    "High Traffic": 50
}

# Initialize Q-Tables
DQN = {}
DDQN = {}
DUELING = {}
PER = {}

for state in states:
    DQN[state] = {}
    DDQN[state] = {}
    DUELING[state] = {}
    PER[state] = {}

    for action in actions:
        DQN[state][action] = 0
        DDQN[state][action] = 0
        DUELING[state][action] = 0
        PER[state][action] = 0

# Parameters
alpha = 0.5
gamma = 0.9
episodes = 200

# Training
for episode in range(episodes):

    for state in states:

        reward = reward_table[state]

        for action in actions:

            # DQN
            DQN[state][action] += alpha * (
                reward + gamma * max(DQN[state].values()) - DQN[state][action]
            )

            # DDQN
            DDQN[state][action] += alpha * (
                reward + gamma * max(DDQN[state].values()) - DDQN[state][action]
            )

            # Dueling DQN
            DUELING[state][action] += alpha * (
                reward + gamma * max(DUELING[state].values()) - DUELING[state][action]
            )

            # PER (Higher priority for High Traffic)
            priority = 2 if state == "High Traffic" else 1

            PER[state][action] += alpha * priority * (
                reward + gamma * max(PER[state].values()) - PER[state][action]
            )

# Display Results
print("Traffic Signal Optimization")
print("----------------------------------")

for state in states:

    print("\nState :", state)

    print("DQN      :", round(max(DQN[state].values()), 2))
    print("DDQN     :", round(max(DDQN[state].values()), 2))
    print("Dueling  :", round(max(DUELING[state].values()), 2))
    print("PER      :", round(max(PER[state].values()), 2))

# Best action
print("\nOptimal Signal Decisions")
print("----------------------------------")

for state in states:

    action = max(DQN[state], key=DQN[state].get)

    print(state, "-->", action)
