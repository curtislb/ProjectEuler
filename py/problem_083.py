#!/usr/bin/env python3

"""problem_083.py

Problem 83: Path sum: four ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by moving left, right, up, and down, is indicated by parentheses
and is equal to 2297.

    (131)  673  (234) (103)  (18)
    (201)  (96) (342)  965  (150)
     630   803   746  (422) (111)
     537   699   497  (121)  956
     805   732   524   (37) (331)

Find the minimal path sum in INPUT_FILE, a text file containing a square
matrix, from the top left to the bottom right by moving left, right, up, and
down.

Author: Curtis Belmonte
"""

import common.fileio as fio
from common.utility import Graph


# PARAMETERS ##################################################################


INPUT_FILE = '../input/083.txt' # default: '../input/083.txt'


# SOLUTION ####################################################################


def solve() -> int:
    matrix = list(fio.ints_from_file(INPUT_FILE, sep=','))
    n = len(matrix)
    
    # create graph with virtual start nodes
    graph = Graph()
    start_node = (-1, -1)
    graph.add_node(start_node)

    # add all (row, col) pairs in matrix as nodes
    for i in range(n):
        for j in range(n):
            graph.add_node((i, j))

    # connect virtual start node to top-left node in matrix
    graph.add_edge(start_node, (0, 0), matrix[0][0])

    # add edges to each node going up, down, left, and right
    for i in range(n):
        for j in range(n):
            node = (i, j)
            graph.try_add_matrix_edge(matrix, node, i - 1, j) # above
            graph.try_add_matrix_edge(matrix, node, i + 1, j) # below
            graph.try_add_matrix_edge(matrix, node, i, j - 1) # left
            graph.try_add_matrix_edge(matrix, node, i, j + 1) # right

    distance, _ = graph.dijkstra(start_node)
    goal_node = (n - 1, n - 1)
    return int(distance[goal_node])


if __name__ == '__main__':
    print(solve())
