#!/usr/bin/env python3

"""problem_082.py

Problem 82: Path sum: three ways

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the
left column and finishing in any cell in the right column, and only moving up,
down, and right, is indicated by parentheses; the sum is equal to 994.

     131   673  (234) (103)  (18)
    (201)  (96) (342)  965   150
     630   803   746   422   111
     537   699   497   121   956
     805   732   524    37   331

Find the minimal path sum in INPUT_FILE, a text file containing a square
matrix, from the left column to the right column.

Author: Curtis Belmonte
"""

import common.fileio as fio
from common.utility import Graph


# PARAMETERS ##################################################################


INPUT_FILE = '../input/082.txt' # default: '../input/082.txt'


# SOLUTION ####################################################################


def solve() -> int:
    matrix = list(fio.ints_from_file(INPUT_FILE, sep=','))
    n = len(matrix)
    
    # create graph with virtual start and goal nodes
    graph = Graph()
    start_node = (-1, -1)
    goal_node = (n, n)
    graph.add_node(start_node)
    graph.add_node(goal_node)

    # connect virtual start node to nodes in left column
    for i, row in enumerate(matrix):
        node = (i, 0)
        graph.add_node(node)
        graph.add_edge(start_node, node, row[0])

    # add all (row, col) pairs in matrix as nodes
    for i in range(n):
        for j in range(1, n):
            graph.add_node((i, j))

    # add edges to each node going up, down, and right
    for i in range(n):
        for j in range(n):
            node = (i, j)
            graph.try_add_matrix_edge(matrix, node, i - 1, j) # above
            graph.try_add_matrix_edge(matrix, node, i + 1, j) # below
            graph.try_add_matrix_edge(matrix, node, i, j + 1) # right

    # connect nodes in right column to virtual goal node
    for i in range(n):
        node = (i, n - 1)
        graph.add_edge(node, goal_node, 0)

    distance, _ = graph.dijkstra(start_node)
    return int(distance[goal_node])


if __name__ == '__main__':
    print(solve())
