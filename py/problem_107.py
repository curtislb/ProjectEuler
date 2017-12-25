#!/usr/bin/env python3

"""problem_107.py

Problem 107: Minimal network

The following undirected network consists of seven vertices and twelve edges
with a total weight of 243.

    	A	B	C	D	E	F	G
    A	-	16	12	21	-	-	-
    B	16	-	-	17	20	-	-
    C	12	-	-	28	-	31	-
    D	21	17	28	-	18	19	23
    E	-	20	-	18	-	-	11
    F	-	-	31	19	-	-	27
    G	-	-	-	23	11	27	-

However, it is possible to optimise the network by removing some edges and
still ensure that all points on the network remain connected. The network which
achieves the maximum saving has a weight of 93, representing a saving of 243 −
93 = 150 from the original network.

Using INPUT_FILE, a text file containing a network given in matrix form, find
the maximum saving which can be achieved by removing redundant edges whilst
ensuring that the network remains connected.
"""

__author__ = 'Curtis Belmonte'

import common.fileio as fio
from common.utility import Graph


# PARAMETERS ##################################################################


INPUT_FILE = '../input/107.txt' # default: '../input/107.txt'


# SOLUTION ####################################################################


def solve() -> int:
    # initialize network graph from file
    matrix = fio.ints_from_file(INPUT_FILE, sep=',')
    graph = Graph()
    total_weight = 0
    for i, row in enumerate(matrix):
        for j, weight in enumerate(row):
            # add node labels if not already in graph
            if not graph.has_node(i):
                graph.add_node(i)
            if not graph.has_node(j):
                graph.add_node(j)

            # add non-zero edges to graph and total
            if weight != 0:
                graph.add_edge(i, j, weight)
                total_weight += weight

    # halve total weight, since edges are double-counted
    total_weight //= 2

    # find and calculate weight for minimum spanning tree
    mst_edges = graph.prim_mst()
    mst_weight = 0
    for u, v in mst_edges:
        mst_weight += graph.edge_weight(u, v)

    # return amount saved by minimum spanning tree
    return total_weight - mst_weight


if __name__ == '__main__':
    print(solve())
