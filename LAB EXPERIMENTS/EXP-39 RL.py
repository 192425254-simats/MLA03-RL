import random

print("RL-Based Healthcare Management")
print("--------------------------------")

patients = 20
total_reward = 0

for episode in range(1, 101):

    waiting_time = 0
    reward = 0

    for patient in range(patients):

        action = random.choice([
            "FAST",
            "NORMAL",
            "DELAY"
        ])

        if action == "FAST":
            waiting_time += 1
            reward += 5

        elif action == "NORMAL":
            waiting_time += 3
            reward += 3

        else:
            waiting_time += 6
            reward -= 2

    total_reward += reward

    if episode % 20 == 0:
        print(
            "Episode:", episode,
            "Waiting Time:", waiting_time,
            "Reward:", reward
        )

print("\nTraining completed.")
print("Total Reward:", total_reward)
print("Healthcare scheduling policy evaluated.")
