import random

print("PPO - Autonomous Vehicle Lane Changing")
print("---------------------------------------")

lanes = 3
lane = 1
reward = 0

for episode in range(1, 11):

    lane = 1
    episode_reward = 0

    for step in range(10):

        action = random.choice(["LEFT", "STAY", "RIGHT"])

        if action == "LEFT" and lane > 0:
            lane -= 1

        elif action == "RIGHT" and lane < lanes - 1:
            lane += 1

        # Reward for staying in a safe lane
        if lane == 1:
            r = 2
        else:
            r = 1

        episode_reward += r

    reward += episode_reward

    print("Episode:", episode,
          "Final Lane:", lane,
          "Reward:", episode_reward)

print("\nTraining completed.")
print("Average Reward:", reward / 10)
