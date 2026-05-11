# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Initial State
state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Function to print puzzle
def print_puzzle(state):

    for row in state:

        for value in row:

            if value == 0:
                print("_", end=" ")

            else:
                print(value, end=" ")

        print()

# Heuristic Function
# Count misplaced tiles
def heuristic(state):

    count = 0

    for i in range(3):

        for j in range(3):

            if state[i][j] != 0 and state[i][j] != goal[i][j]:

                count += 1

    return count


print("Initial State:\n")

print_puzzle(state)

h = heuristic(state)

print("\nHeuristic Value =", h)