print("Bellman's Optimality Equation")
print("-----------------------------")

grid = [
    [0, 0, 0],
    [0, -1, 0],
    [0, 0, 10]
]

rows = 3
cols = 3

value = [[0 for j in range(cols)] for i in range(rows)]

goal = (2, 2)

# Value iteration
for iteration in range(20):

    new_value = [row[:] for row in value]

    for i in range(rows):
        for j in range(cols):

            if (i, j) == goal:
                new_value[i][j] = 10
                continue

            if grid[i][j] == -1:
                continue

            neighbours = []

            if i > 0:
                neighbours.append(value[i - 1][j])

            if i < rows - 1:
                neighbours.append(value[i + 1][j])

            if j > 0:
                neighbours.append(value[i][j - 1])

            if j < cols - 1:
                neighbours.append(value[i][j + 1])

            new_value[i][j] = -1 + 0.9 * max(neighbours)

    value = new_value

print("Optimal State Values:")

for row in value:
    print([round(x, 2) for x in row])

print("\nOptimal Path:")

position = (0, 0)
path = [position]

while position != goal:

    i, j = position
    best = None
    best_value = -999

    neighbours = []

    if i > 0:
        neighbours.append((i - 1, j))

    if i < rows - 1:
        neighbours.append((i + 1, j))

    if j > 0:
        neighbours.append((i, j - 1))

    if j < cols - 1:
        neighbours.append((i, j + 1))

    for n in neighbours:

        if grid[n[0]][n[1]] == -1:
            continue

        if value[n[0]][n[1]] > best_value:
            best_value = value[n[0]][n[1]]
            best = n

    if best is None:
        break

    position = best
    path.append(position)

print(path)
