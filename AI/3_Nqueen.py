def print_board(board, n):

    for i in range(n):

        for j in range(n):

            if board[i] == j:
                print("Q", end=" ")

            else:
                print(".", end=" ")

        print()


def is_safe(board, row, col):

    for i in range(row):

        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col):

            board[row] = col

            if solve(board, row + 1, n):
                return True

    return False


n = int(input("Enter number of queens: "))

board = [-1] * n

if solve(board, 0, n):

    print("Solution Found:\n")

    print_board(board, n)

else:
    print("No Solution")