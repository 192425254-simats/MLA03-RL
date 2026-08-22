import random

print("RL-Based Personalized Education")
print("--------------------------------")

levels = ["EASY", "MEDIUM", "HARD"]

total_reward = 0

for episode in range(1, 101):

    student_level = random.choice(levels)
    reward = 0

    for step in range(10):

        # Select learning content
        action = random.choice(levels)

        if action == student_level:
            reward += 5
        elif action == "MEDIUM":
            reward += 3
        else:
            reward += 1

        # Student learning progress
        if reward >= 25:
            student_level = "HARD"

    total_reward += reward

    if episode % 20 == 0:
        print(
            "Episode:", episode,
            "Student Level:", student_level,
            "Reward:", reward
        )

print("\nTraining completed.")
print("Total Reward:", total_reward)
print("Personalized learning policy evaluated.")
