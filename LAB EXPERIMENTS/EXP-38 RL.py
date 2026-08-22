import random

print("POMDP - Robot Navigation")
print("-------------------------")

locations = ["A", "B", "C", "D"]
actual_location = random.choice(locations)

reward = 0

for step in range(1, 11):

    # Partial observation
    observation = random.choice(locations)

    print(
        "Step:", step,
        "Observation:", observation
    )

    if observation == actual_location:
        reward += 5
    else:
        reward -= 1

    # Robot moves
    actual_location = random.choice(locations)

print("\nNavigation completed.")
print("Total Reward:", reward)
