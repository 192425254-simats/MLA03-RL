import random

print("REINFORCE - Automated Trading")
print("-----------------------------")

actions = ["BUY", "SELL", "HOLD"]
total_profit = 0

for episode in range(1, 11):

    profit = 0

    for step in range(10):

        price_change = random.choice([-2, -1, 1, 2])
        action = random.choice(actions)

        if action == "BUY":
            reward = price_change

        elif action == "SELL":
            reward = -price_change

        else:
            reward = 0

        profit += reward

    total_profit += profit

    print("Episode:", episode,
          "Profit:", profit)

print("\nTraining completed.")
print("Total Profit:", total_profit)
