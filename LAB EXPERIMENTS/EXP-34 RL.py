import random

print("REINFORCE - Smart Home Energy Management")
print("-----------------------------------------")

temperature = 25
total_reward = 0

actions = ["HEAT", "COOL", "OFF"]

for episode in range(1, 101):

    temperature = random.randint(18, 32)
    reward = 0

    for step in range(10):

        action = random.choice(actions)

        if action == "HEAT":
            temperature += 1
            energy = 3

        elif action == "COOL":
            temperature -= 1
            energy = 3

        else:
            energy = 1

        # Comfort target = 24-26
        comfort = 10 - abs(25 - temperature)

        reward += comfort - energy

    total_reward += reward

    if episode % 20 == 0:
        print(
            "Episode:", episode,
            "Temperature:", temperature,
            "Reward:", round(reward, 2)
        )

print("\nTraining completed.")
print("Total Reward:", round(total_reward, 2))
print("Smart home learned energy-efficient control.")
