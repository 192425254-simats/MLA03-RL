import random

# Number of advertisements
ads = ["Ad A", "Ad B", "Ad C"]

# True click probabilities (unknown to the agent)
click_probabilities = [0.3, 0.6, 0.8]

# Initialize values
Q = [0.0, 0.0, 0.0]      # Estimated reward for each ad
N = [0, 0, 0]            # Number of times each ad is selected

# Parameters
epsilon = 0.2
iterations = 1000

# Training
for i in range(iterations):

    # Exploration or Exploitation
    if random.random() < epsilon:
        action = random.randint(0, 2)
    else:
        action = Q.index(max(Q))

    # Simulate user click
    if random.random() < click_probabilities[action]:
        reward = 1
    else:
        reward = 0

    # Update count
    N[action] += 1

    # Update estimated reward
    Q[action] = Q[action] + (1 / N[action]) * (reward - Q[action])

# Display results
print("Advertisement Statistics")
print("-----------------------------")

for i in range(3):
    print("Advertisement :", ads[i])
    print("Times Selected :", N[i])
    print("Estimated Reward :", round(Q[i], 3))
    print()

best_ad = ads[Q.index(max(Q))]

print("-----------------------------")
print("Best Advertisement :", best_ad)
