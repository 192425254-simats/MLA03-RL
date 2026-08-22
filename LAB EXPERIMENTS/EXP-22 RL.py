import random

print("Q-Learning Grid Game")
print("--------------------")

# Grid size
size = 5

# Start and goal
start = (0, 0)
goal = (4, 4)

# Q-table
q = {}

actions = ["UP", "DOWN", "LEFT", "RIGHT"]

# Get Q-value
def get_q(state, action):
    return q.get((state, action), 0)


# Training
for episode in range(1000):

    state = start

    for step in range(50):

        # Choose random action
        action = random.choice(actions)

        row, col = state

        # Move
        if action == "UP":
            row -= 1
        elif action == "DOWN":
            row += 1
        elif action == "LEFT":
            col -= 1
        elif action == "RIGHT":
            col += 1

        # Check boundary
        if row < 0 or row >= size or col < 0 or col >= size:
            next_state = state
            reward = -5

        else:
            next_state = (row, col)

            if next_state == goal:
                reward = 10
            else:
                reward = -1

        # Q-learning update
        old_q = get_q(state, action)

        future_q = max(
            get_q(next_state, a)
            for a in actions
        )

        new_q = old_q + 0.1 * (
            reward + 0.9 * future_q - old_q
        )

        q[(state, action)] = new_q

        state = next_state

        if state == goal:
            break


# Test trained agent
print("\nTraining completed.")
print("\nAI Path:")

state = start
path = [state]

for step in range(20):

    best_action = max(
        actions,
        key=lambda a: get_q(state, a)
    )

    row, col = state

    if best_action == "UP":
        row -= 1
    elif best_action == "DOWN":
        row += 1
    elif best_action == "LEFT":
        col -= 1
    else:
        col += 1

    if 0 <= row < size and 0 <= col < size:
        state = (row, col)
        path.append(state)

    if state == goal:
        break

print(path)

if state == goal:
    print("\nAI reached the goal successfully!")
else:
    print("\nAI did not reach the goal.")
