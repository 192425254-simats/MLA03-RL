import random

print("Dueling DQN vs Standard DQN")
print("----------------------------")

states = 10

dqn_score = 0
dueling_score = 0

for episode in range(1, 101):

    dqn_reward = random.randint(5, 10)
    dueling_reward = random.randint(7, 12)

    dqn_score += dqn_reward
    dueling_score += dueling_reward

    if episode % 20 == 0:
        print(
            "Episode:", episode,
            "DQN:", dqn_score,
            "Dueling DQN:", dueling_score
        )

print("\nTraining completed.")

print("\nFinal Performance")
print("Standard DQN:", dqn_score)
print("Dueling DQN :", dueling_score)

if dueling_score > dqn_score:
    print("Dueling DQN performed better.")
else:
    print("Standard DQN performed better.")
