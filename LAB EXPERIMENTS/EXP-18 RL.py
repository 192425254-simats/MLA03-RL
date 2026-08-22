import random

print("Meta-Reinforcement Learning")
print("---------------------------")

tasks = ["Pick", "Place", "Sort"]

learning_rate = 0.1
performance = 0

for episode in range(1, 101):

    task = random.choice(tasks)

    if task == "Pick":
        reward = random.randint(7, 10)
    elif task == "Place":
        reward = random.randint(6, 10)
    else:
        reward = random.randint(5, 10)

    performance = performance + learning_rate * (reward - performance)

    if episode % 20 == 0:
        print("Episode:", episode,
              "Task:", task,
              "Reward:", reward,
              "Performance:", round(performance, 2))

print("\nTraining Completed")
print("Robot adapted to new tasks quickly.")
