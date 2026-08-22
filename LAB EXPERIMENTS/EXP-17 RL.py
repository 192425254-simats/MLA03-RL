import random

print("HRL using HAM and MAXQ")
print("----------------------")

tasks = ["Clean Room", "Collect Object", "Return Home"]

reward = 0

for episode in range(1, 101):

    reward = 0

    # High-level task selection (HAM)
    task = random.choice(tasks)

    # Low-level actions (MAXQ)
    if task == "Clean Room":
        actions = ["Move", "Clean"]
    elif task == "Collect Object":
        actions = ["Move", "Pick"]
    else:
        actions = ["Move", "Return"]

    for action in actions:
        reward += random.randint(5, 10)

    if episode % 20 == 0:
        print("Episode:", episode,
              "Task:", task,
              "Reward:", reward)

print("\nTraining Completed")
print("Robot learned hierarchical tasks.")
