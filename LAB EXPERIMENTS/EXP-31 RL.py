import random

print("SARSA - Tic-Tac-Toe Learning")
print("-----------------------------")

q = {}
actions = list(range(9))

def get_q(state, action):
    return q.get((state, action), 0)

for episode in range(1000):

    state = tuple([" "] * 9)

    for step in range(20):

        available = [
            i for i in range(9)
            if state[i] == " "
        ]

        if not available:
            break

        action = random.choice(available)

        board = list(state)
        board[action] = "X"
        next_state = tuple(board)

        reward = 1

        if len(available) == 1:
            reward = 10

        old_q = get_q(state, action)

        next_actions = [
            i for i in range(9)
            if next_state[i] == " "
        ]

        if next_actions:
            next_action = random.choice(next_actions)
            next_q = get_q(next_state, next_action)
        else:
            next_q = 0

        # SARSA update
        q[(state, action)] = old_q + 0.1 * (
            reward + 0.9 * next_q - old_q
        )

        state = next_state

print("Training completed.")
print("Learned states:", len(q))
print("SARSA agent learned Tic-Tac-Toe actions.")
