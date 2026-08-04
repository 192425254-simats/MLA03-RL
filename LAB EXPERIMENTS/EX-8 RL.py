import random

# States (Rooms)
states = ["Living Room", "Kitchen", "Bedroom", "Charging Station"]

# Rewards
rewards = {
    "Living Room": 10,
    "Kitchen": 20,
    "Bedroom": 30,
    "Charging Station": 50
}

# Possible transitions
transitions = {
    "Living Room": "Kitchen",
    "Kitchen": "Bedroom",
    "Bedroom": "Charging Station",
    "Charging Station": "Charging Station"
}

# State values
returns = {}
visits = {}

for state in states:
    returns[state] = 0
    visits[state] = 0

episodes = 100

# Monte Carlo Training
for episode in range(episodes):

    current_state = "Living Room"
    episode_states = []
    total_reward = 0

    while current_state != "Charging Station":

        episode_states.append(current_state)

        next_state = transitions[current_state]

        total_reward += rewards[next_state]

        current_state = next_state

    episode_states.append("Charging Station")

    # Update state values
    for state in episode_states:
        visits[state] += 1
        returns[state] += total_reward

# Display Results
print("Monte Carlo State Values")
print("-----------------------------")

for state in states:
    value = returns[state] / visits[state]
    print(state, ":", round(value, 2))

# Display Cleaning Path
print("\nOptimal Cleaning Path")
print("-----------------------------")

current_state = "Living Room"

print(current_state, end="")

while current_state != "Charging Station":

    current_state = transitions[current_state]
    print(" -->", current_state, end="")

print("\n\nCleaning Completed Successfully!")
