import random

# Policy probabilities
left = 0.33
stay = 0.34
right = 0.33

print("Policy Gradient Lane Keeping")
print("----------------------------")

for episode in range(1, 101):

    position = random.uniform(-1, 1)
    total_reward = 0

    for step in range(20):

        # Select action
        r = random.random()

        if r < left:
            action = "LEFT"
            position -= 0.1
        elif r < left + stay:
            action = "STAY"
        else:
            action = "RIGHT"
            position += 0.1

        # Reward
        reward = 1 - abs(position)

        if abs(position) > 1:
            reward = -1

        total_reward += reward

        # Simple policy update
        if abs(position) < 0.3:
            stay += 0.001
        elif position > 0:
            left += 0.001
        else:
            right += 0.001

    # Normalize probabilities
    total = left + stay + right
    left /= total
    stay /= total
    right /= total

    if episode % 20 == 0:
        print("Episode:", episode,
              "Reward:", round(total_reward, 2))

print("\nTraining Completed")
print("Left Probability :", round(left, 2))
print("Stay Probability :", round(stay, 2))
print("Right Probability:", round(right, 2))
