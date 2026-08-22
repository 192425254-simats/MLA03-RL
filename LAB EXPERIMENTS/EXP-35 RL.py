import random

print("Investment Portfolio Value Prediction")
print("--------------------------------------")

portfolios = {
    "Portfolio A": 10000,
    "Portfolio B": 10000,
    "Portfolio C": 10000
}

returns = {
    "Portfolio A": 0.08,
    "Portfolio B": 0.12,
    "Portfolio C": 0.06
}

print("\nPredicted Portfolio Values:\n")

for name in portfolios:

    value = portfolios[name]

    for year in range(5):

        change = returns[name] + random.uniform(-0.02, 0.02)

        value = value * (1 + change)

    print(
        name,
        "-> Predicted Value:",
        round(value, 2)
    )

print("\nPortfolio comparison completed.")
