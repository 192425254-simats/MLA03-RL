import random
import math

print("Dynamic Pricing using Multi-Armed Bandits")
print("-----------------------------------------")

prices = [50, 70, 90]

# Probability of customer buying
buy_probability = [0.80, 0.60, 0.40]

N = 1000


def run_algorithm(name):

    revenue = [0, 0, 0]
    count = [0, 0, 0]
    total_revenue = 0

    for i in range(N):

        if name == "Epsilon-Greedy":

            if random.random() < 0.1:
                choice = random.randint(0, 2)
            else:
                values = []

                for j in range(3):
                    if count[j] == 0:
                        values.append(0)
                    else:
                        values.append(
                            revenue[j] / count[j]
                        )

                choice = values.index(max(values))

        elif name == "UCB":

            if i < 3:
                choice = i
            else:
                values = []

                for j in range(3):
                    average = revenue[j] / count[j]

                    bonus = math.sqrt(
                        2 * math.log(i) / count[j]
                    )

                    values.append(average + bonus)

                choice = values.index(max(values))

        else:

            samples = []

            for j in range(3):

                samples.append(
                    random.betavariate(
                        count[j] + 1,
                        i - count[j] + 1
                    )
                )

            choice = samples.index(max(samples))

        count[choice] += 1

        if random.random() < buy_probability[choice]:

            r = prices[choice]
            revenue[choice] += r
            total_revenue += r

    return total_revenue


eg = run_algorithm("Epsilon-Greedy")
ucb = run_algorithm("UCB")
ts = run_algorithm("Thompson")

print("Epsilon-Greedy Revenue :", eg)
print("UCB Revenue            :", ucb)
print("Thompson Sampling      :", ts)

best = max(
    [("Epsilon-Greedy", eg),
     ("UCB", ucb),
     ("Thompson Sampling", ts)],
    key=lambda x: x[1]
)

print("\nBest Strategy:", best[0])
print("Maximum Revenue:", best[1])
