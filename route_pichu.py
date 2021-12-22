#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [Dhanalakshmi V; nvveer@iu.edu]
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys
import json


# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Check if a row,col index pair is on the map
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    # locD, locU, locL, locR = pos[0], pos[1], pos[2], pos[3]
    # loc0 = [(pos[0], pos[1])][0]
    # loc1 = [(pos[0], pos[1])][1]
    # for x in visited:
    #   if pos not in visited:
    #      print(x)
    return 0 <= pos[0] < n and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
def moves(map, row, col, path):
    moves = [(row + 1, col, path + 'D'), (row - 1, col, path + 'U'), (row, col - 1, path + 'L'),
             (row, col + 1, path + 'R')]

    # move_path = (('D', col), ('U', col), (row, 'L'), (row, 'R'))
    # stance_row = ['L', 0, 0, 'R']
    # stance_col = [0, 'U', 'D', 0]
    # move=0
    # for move in moves :
    #    if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@"):
    #       print(move)
    # Return only moves that are within the board and legal (i.e. go through open space ".")
    return [move for move in moves if
            valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]


# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#
def search(house_map):
    # Find pichu start position
    # visited = [[False for x in range(N)] for y in range(M)]
    pichu_loc = [(row_i, col_i)
                 for col_i in range(len(house_map[0]))
                 for row_i in range(len(house_map))
                 if house_map[row_i][col_i] == "p"][0]
    fringe = [(pichu_loc, 0, '')]
    reached = []
    move_string = ''
    while fringe:
        (curr_move, curr_dist, move_string) = fringe.pop()
        # if curr_move not in visited:
        reached.append(curr_move)
        for move in moves(house_map, *curr_move, move_string):
            if house_map[move[0]][move[1]] == "@":
                return curr_dist + 1, move[2]  # return a dummy answer
            else:
                if (move[0], move[1]) not in reached:
                    fringe.append(((move[0], move[1]), curr_dist + 1, move[2]))
    if len(fringe) == 0:
        return -1, ""


# def path(visited):
#   for x in visited:
#      print(x)


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    print("Routing in this board:\n" + printable_board(house_map) + "\n")
    print("Shhhh... quiet while I navigate!")
    # M = N = 10 Trying with Matrix format
    # reached = (row_r, col_r)
    # searched = [(reached), 0]
    solution = search(house_map)
    print("Here's the solution I found:")
    print(str(solution[0]) + " " + str(solution[1]))
