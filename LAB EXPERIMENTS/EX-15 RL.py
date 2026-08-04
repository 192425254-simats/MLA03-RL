import random

# States
states = ["Start", "Step1", "Step2", "Goal"]

# Actions
actions = ["Walk", "Balance"]

# Rewards
rewards = {
    "Start": 0,
    "Step1": 20,
    "Step2": 40,
    "Goal": 100
}

# Policy values
ppo_policy = {}
trpo_policy = {}

for state in states:
    ppo_policy[state] = {}
    trpo_policy[state] = {}

    for action in actions:
        ppo_policy[state][action] = 0.5
        trpo_policy[state][action] = 0.5

alpha = 0.1
episodes = 100

# Training
for episode in range(episodes):

    state = "Start"

    while state != "Goal":

        # PPO selects action
        if random.random() < ppo_policy[state]["Walk"]:
            action = "Walk"
        else:
            action = "Balance"

        # State transition
        if state == "Start":
            next_state = "Step1"

        elif state == "Step1":
            next_state = "Step2"

        elif state == "Step2":
            next_state = "Goal"

        reward = rewards[next_state]

        # PPO Update (Limited update)
        ppo_policy[state][action] += alpha * (reward / 100)
        if ppo_policy[state][action] > 1:
            ppo_policy[state][action] = 1

        # TRPO Update (Smaller trusted update)
        trpo_policy[state][action] += (alpha / 2) * (reward / 100)
        if trpo_policy[state][action] > 1:
            trpo_policy[state][action] = 1

        state = next_state

# Display PPO Policy
print("PPO Policy")
print("----------------------")

for state in states:
    print(state, ":", ppo_policy[state])

# Display TRPO Policy
print("\nTRPO Policy")
print("----------------------")

for state in states:
    print(state, ":", trpo_policy[state])

# Test Walking
print("\nHumanoid Walking")
print("----------------------")

state = "Start"
print(state)

while state != "Goal":

    action = max(ppo_policy[state], key=ppo_policy[state].get)

    print("Action :", action)

    if state == "Start":
        state = "Step1"

    elif state == "Step1":
        state = "Step2"

    elif state == "Step2":
        state = "Goal"

    print("Next State :", state)

print("\nHumanoid Reached Goal Successfully!")
