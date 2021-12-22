#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [Dhanalakshmi V ; nvveer@iu.edu]
#
# Based on skeleton code in CSCI B551, Spring 2021
#


import sys


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Add a pichu to the board at the given position, and return a new board (doesn't change original)
def add_pichu(board, row, col):
    return (board[0:row] + [board[row][0:col] + ['p'] + board[row][col+1:]] + board[row+1:])

# Count total # of pichus on board
def count_pichus(board):
    n = sum([row.count('p') for row in board])
    return n


# check if board is a goal state
def is_goal(board, temp_k):
    if count_pichus(board) == temp_k:
        return True


# Get list of successors of given board state
def successors(board):
    n = len(board)
    m = len(board[0])
    return listofSuc(board, n, m)


def listofSuc(mid_board, row, col):
    success_states = []
    for r in range(row):
        for c in range(col):
            valid = True
            if mid_board[r][c] != '.':
                continue
            # create directions
            view = [[mid_board[a][c] for a in range(r - 1, -1, -1)],
                    [mid_board[a][c] for a in range(r + 1, row)],
                    [mid_board[r][b] for b in range(c - 1, -1, -1)],
                    [mid_board[r][b] for b in range(c + 1, col)]]

            for pair in view:
                line = "".join(pair)
                if line == "":
                    continue
                # find the character's index
                block = line.find("X")
                goal = line.find("@")
                start = line.find("p")

                if start != -1:
                    if block == -1 and goal == -1:
                        valid = False
                        break
                    elif block == -1 and goal != -1 and goal > start:
                        valid = False
                        break
                    elif block != -1 and goal == -1 and block > start:
                        valid = False
                        break
                    elif min(block, goal) > start:
                        valid = False
                        break
            # valid successor board
            if valid:
                new = add_pichu(mid_board, r, c)
                success_states.append(new)
    return success_states


# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, k):
    fringe = [initial_board]
    reached = []
    while len(fringe)>0:
        curr_move = fringe.pop()
        # condition for exit
        if is_goal(curr_move, k):
            return (curr_move, True)
        for suc in successors(curr_move):
            # To avoid already visited states
            if suc in reached:
                continue
            reached.append(suc)
            fringe.append(suc)
    return ([], False)


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    k = int(sys.argv[2])# This is K, the number of agents
    print("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)
    print("Here's what we found:")
    print(printable_board(newboard) if success else "None")
