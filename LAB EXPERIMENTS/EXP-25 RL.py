import random
import math

print("Multi-Armed Bandit Algorithms")
print("-----------------------------")

# True click probabilities
probabilities = [0.20, 0.40, 0.30]

N = 1000


# --------------------------------
# Epsilon-Greedy
# --------------------------------

def epsilon_greedy():

    clicks = [0, 0, 0]
    shows = [0, 0, 0]

    for i in range(N):

        if random.random() < 0.1:
            ad = random.randint(0, 2)
        else:
            rates = []

            for j in range(3):
                if shows[j] == 0:
                    rates.append(0)
                else:
                    rates.append(clicks[j] / shows[j])

            ad = rates.index(max(rates))

        shows[ad] += 1

        if random.random() < probabilities[ad]:
            clicks[ad] += 1

    return sum(clicks) / N


# --------------------------------
# UCB
# --------------------------------

def ucb():

    clicks = [0, 0, 0]
    shows = [0, 0, 0]

    for ad in range(3):
        shows[ad] += 1
        if random.random() < probabilities[ad]:
            clicks[ad] += 1

    for i in range(3, N):

        values = []

        for ad in range(3):

            average = clicks[ad] / shows[ad]

            bonus = math.sqrt(
                2 * math.log(i) / shows[ad]
            )

            values.append(average + bonus)

        ad = values.index(max(values))

        shows[ad] += 1

        if random.random() < probabilities[ad]:
            clicks[ad] += 1

    return sum(clicks) / N


# --------------------------------
# Thompson Sampling
# --------------------------------

def thompson():

    success = [1, 1, 1]
    failure = [1, 1, 1]

    total_clicks = 0

    for i in range(N):

        samples = []

        for ad in range(3):

            sample = random.betavariate(
                success[ad],
                failure[ad]
            )

            samples.append(sample)

        ad = samples.index(max(samples))

        if random.random() < probabilities[ad]:
            success[ad] += 1
            total_clicks += 1
        else:
            failure[ad] += 1

    return total_clicks / N


eg = epsilon_greedy()
u = ucb()
ts = thompson()

print("Epsilon-Greedy CTR :", round(eg, 3))
print("UCB CTR            :", round(u, 3))
print("Thompson Sampling  :", round(ts, 3))

best = max(
    [("Epsilon-Greedy", eg),
     ("UCB", u),
     ("Thompson Sampling", ts)],
    key=lambda x: x[1]
)

print("\nBest Algorithm:", best[0])
print("Highest CTR:", round(best[1], 3))
