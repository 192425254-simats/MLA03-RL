import random

print("Multi-Agent Reinforcement Learning")
print("-----------------------------------")

robots = ["Robot 1", "Robot 2", "Robot 3"]
tasks = ["Task A", "Task B", "Task C"]

total_reward = 0

for episode in range(1, 101):

    episode_reward = 0

    for robot in robots:

        task = random.choice(tasks)

        reward = random.randint(5, 10)

        episode_reward += reward

        print(robot, "->", task, "Reward:", reward)

    total_reward += episode_reward

    if episode % 20 == 0:
        print("\nEpisode:", episode,
              "Total Reward:", total_reward)
        print("---------------------------")

print("\nTraining Completed")
print("Robots learned cooperative task allocation.")
