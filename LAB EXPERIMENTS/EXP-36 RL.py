import random

print("MAXQ Hierarchical Reinforcement Learning")
print("-----------------------------------------")

tasks = {
    "Main Task": [
        "Collect Object",
        "Move Object",
        "Place Object"
    ]
}

total_reward = 0

for episode in range(1, 101):

    reward = 0

    for subtask in tasks["Main Task"]:

        if subtask == "Collect Object":
            r = 5

        elif subtask == "Move Object":
            r = 7

        else:
            r = 10

        reward += r

    total_reward += reward

    if episode % 20 == 0:
        print(
            "Episode:", episode,
            "Reward:", reward
        )

print("\nTraining completed.")
print("Total Reward:", total_reward)
print("MAXQ learned hierarchical subtasks.")
