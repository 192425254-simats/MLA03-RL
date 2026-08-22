import random

print("DQN - Autonomous Highway Vehicle")
print("---------------------------------")

actions = ["LEFT", "STAY", "RIGHT"]

q_table = {}

learning_rate = 0.1
discount = 0.9

for episode in range(1, 101):

    state = random.randint(0, 2)
    total_reward = 0

    for step in range(10):

        # Choose action
        action = random.choice(actions)

        if state not in q_table:
            q_table[state] = {
                "LEFT": 0,
                "STAY": 0,
                "RIGHT": 0
            }

        # Simulated environment
        next_state = random.randint(0, 2)

        if next_state == 1:
            reward = 5
        else:
            reward = 1

        # DQN-style Q update
        old_value = q_table[state][action]

        max_future = max(
            q_table.get(
                next_state,
                {"LEFT": 0, "STAY": 0, "RIGHT": 0}
            ).values()
        )

        new_value = old_value + learning_rate * (
            reward +
            discount * max_future -
            old_value
        )

        q_table[state][action] = new_value

        state = next_state
        total_reward += reward

    if episode % 20 == 0:
        print("Episode:", episode,
              "Reward:", total_reward)

print("\nTraining Completed")

print("\nLearned Q-Values:")

for state in q_table:
    print("State", state, q_table[state])

print("\nDQN agent learned driving actions.")
