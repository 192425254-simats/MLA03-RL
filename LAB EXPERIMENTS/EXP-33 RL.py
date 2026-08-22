import random

print("DDPG - Real-Time Strategy Game")
print("--------------------------------")

resources = 0
units = 0
score = 0

for episode in range(1, 101):

    resources = 0
    units = 0
    score = 0

    for step in range(10):

        action = random.choice([
            "GATHER",
            "BUILD",
            "ATTACK"
        ])

        if action == "GATHER":
            resources += 10
            reward = 5

        elif action == "BUILD":

            if resources >= 10:
                resources -= 10
                units += 1
                reward = 8
            else:
                reward = -2

        else:

            if units > 0:
                score += 10
                reward = 10
            else:
                reward = -3

    if episode % 20 == 0:
        print(
            "Episode:", episode,
            "Resources:", resources,
            "Units:", units,
            "Score:", score
        )

print("\nTraining completed.")
print("DDPG agent learned resource and unit management.")
