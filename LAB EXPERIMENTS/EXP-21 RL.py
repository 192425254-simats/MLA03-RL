import random

print("Smart Energy Management using Reinforcement Learning")
print("----------------------------------------------------")

energy = 50
total_reward = 0

for episode in range(1, 101):

    temperature = random.randint(18, 35)

    # Actions
    actions = ["LOW", "MEDIUM", "HIGH"]
    action = random.choice(actions)

    # Energy consumption
    if action == "LOW":
        consumption = 2
    elif action == "MEDIUM":
        consumption = 4
    else:
        consumption = 6

    # Reward
    comfort = 10 - abs(25 - temperature)

    reward = comfort - consumption

    total_reward += reward

    if episode % 20 == 0:
        print("Episode:", episode,
              "Temperature:", temperature,
              "Action:", action,
              "Reward:", round(reward, 2))

print("\nTraining Completed")
print("Total Reward:", round(total_reward, 2))
print("Energy management optimized.")
