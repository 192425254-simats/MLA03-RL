import random

print("POMDP Search and Rescue Robot")
print("-----------------------------")

# Possible locations
locations = ["Room 1", "Room 2", "Room 3", "Room 4"]

# Hidden victim location
victim = random.choice(locations)

reward = 0

for step in range(1, 11):

    # Robot has partial observation
    observation = random.choice(locations)

    print("Step:", step, "Robot observes:", observation)

    # Robot chooses an action
    action = random.choice(["Search", "Move"])

    if action == "Search":

        if observation == victim:
            reward += 10
            print("Victim found!")
            break
        else:
            reward -= 1

    else:
        reward += 1

print("\nTotal Reward:", reward)
print("Search completed.")
