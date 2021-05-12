# Name: Jamar Hill
# Date: 5/10/2021
# Description: CS 162 Project 6d

# row = [2, 4, 5, 3, 1, 3, 1, 4, 0]
#              ^
# pos = 2
# visited = [True, False, True, False, False, False, False, False, False]
def row_puzzle_rec(row, pos, visited):
    # 3 Base cases

    # If position index out of bounds, return false
    if pos < 0 or pos > len(row) - 1:
        return False

    # If value of the square is 0, check two things: square is either last one or not the last one
    if row[pos] == 0:
        if pos == len(row) - 1:
            return True
        return False

    if visited[pos] == True:  # If we have already been to this square then not possible
        return False

    else:
        visited[pos] = True
        # Recursive in both left and right directions
        return row_puzzle_rec(row, pos - row[pos], visited) or row_puzzle_rec(row, pos + row[pos], visited)


def row_puzzle(row):
    # Makes a list of False values
    visited = [False for item in range(len(row))]
    return row_puzzle_rec(row, 0, visited)


successfulPuzzle = row_puzzle([2, 4, 5, 3, 1, 3, 1, 4, 0])
print(successfulPuzzle)
successfulPuzzle = row_puzzle([1, 3, 2, 1, 3, 4, 0])
print(successfulPuzzle)