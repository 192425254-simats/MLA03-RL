print("Autonomous Car Road Navigation")
print("-------------------------------")

road = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
}

current = "A"
destination = "E"

path = [current]

while current != destination:

    next_nodes = road[current]

    # Select first safe road
    current = next_nodes[0]

    path.append(current)

print("Starting Point:", path[0])
print("Destination:", destination)
print("Safe Path:", " -> ".join(path))

print("\nCar reached the destination safely.")
