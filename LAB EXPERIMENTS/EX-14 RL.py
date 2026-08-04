import random

# Floors (States)
states = ["Ground", "Floor1", "Floor2", "Floor3"]

# Actions
actions = ["Up", "Down"]

# Rewards
rewards = {
    "Ground": 0,
    "Floor1": 20,
    "Floor2": 40,
    "Floor3": 100
}

# Actor (Policy)
actor = {}

# Critic (State Value)
critic = {}

for state in states:
    actor[state] = {}
    critic[state] = 0

    for action in actions:
        actor[state][action] = 0.5

# Parameters
alpha_actor = 0.1
alpha_critic = 0.2
gamma = 0.9
episodes = 100

# Training
for episode in range(episodes):

    state = "Ground"

    while state != "Floor3":

        # Actor chooses action
        if random.random() < actor[state]["Up"]:
            action = "Up"
        else:
            action = "Down"

        # Environment
        if state == "Ground":
            next_state = "Floor1"

        elif state == "Floor1":
            next_state = "Floor2"

        elif state == "Floor2":
            next_state = "Floor3"

        reward = rewards[next_state]

        # TD Error (Critic)
        td_error = reward + gamma * critic[next_state] - critic[state]

        # Critic Update
        critic[state] += alpha_critic * td_error

        # Actor Update
        actor[state][action] += alpha_actor * td_error / 100

        state = next_state

# Display Critic Values
print("State Values (Critic)")
print("-----------------------------")

for state in states:
    print(state, ":", round(critic[state], 2))

# Display Actor Policy
print("\nActor Policy")
print("-----------------------------")

for state in states:
    print(state, actor[state])

# Test Elevator
print("\nElevator Route")
print("-----------------------------")

state = "Ground"
print(state)

while state != "Floor3":

    action = max(actor[state], key=actor[state].get)

    print("Action :", action)

    if state == "Ground":
        state = "Floor1"

    elif state == "Floor1":
        state = "Floor2"

    elif state == "Floor2":
        state = "Floor3"

    print("Next State :", state)

print("\nPassenger Reached Destination!")
