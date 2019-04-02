#!/usr/bin/env python3

"""matrices.py

Functions for operating on numerical vectors and matrices.
"""

__author__ = 'Curtis Belmonte'

import copy
from typing import Iterable, List, Optional, Sequence, Tuple

from common.typex import Coord, T


def _try_assign_zeros(matrix: List[List[int]]) -> Sequence[Coord]:
    """Finds as many zeros in matrix as possible with distinct rows and columns.

    The result is a sequence of all unambiguous (row, col) assignments for zero
    values in matrix, such that no row or col value is repeated.
    """

    # convert matrix to bipartite graph, with zeros indicating edges
    edge_matrix = [[value == 0 for value in row] for row in matrix]
    return max_bipartite_matching(edge_matrix)


def _try_bipartite_match(
        edge_matrix: List[List[bool]],
        row: int,
        col_marked: List[bool],
        col_assignments: List[int]) -> bool:

    """Attempts to match the given row to a column in edge_matrix.

    edge_matrix: A boolean matrix indicating edges between rows and columns
    row: Index of the row to attempt to match with a free column
    col_marked: List of marked, or visited, columns for this row
    col_assignments: List of current row assignments for each column, if any

    Returns True if row was successfully matched, or False otherwise.
    """

    # try to match row to each column
    for j in range(len(edge_matrix[0])):

        # check if row can be matched with unmarked column
        if edge_matrix[row][j] and not col_marked[j]:
            col_marked[j] = True

            # check if column is unmatched or can be re-matched with new row
            if col_assignments[j] == -1 or _try_bipartite_match(
                    edge_matrix,
                    col_assignments[j],
                    col_marked,
                    col_assignments):
                col_assignments[j] = row
                return True

    # couldn't match row with any column
    return False


def cross_product_3d(
        p1: Sequence[float],
        p2: Sequence[float]) -> Tuple[float, float, float]:

    """Returns the cross product p1 x p2 of 3-dimensional points p1 and p2."""

    # compute determinant of cross product matrix
    prod_i = (p1[1] * p2[2]) - (p1[2] * p2[1])
    prod_j = (p1[2] * p2[0]) - (p1[0] * p2[2])
    prod_k = (p1[0] * p2[1]) - (p1[1] * p2[0])

    return prod_i, prod_j, prod_k


def dot_product(u: Iterable[float], v: Iterable[float]) -> float:
    """Returns the dot product of vectors u and v."""
    return sum(i * j for i, j in zip(u, v))


def flatten_matrix(matrix: List[List[T]]) -> Sequence[T]:
    """Returns a sequence of the elements in matrix in row-major order."""
    flat_matrix: List[T] = []
    for row in matrix:
        for value in row:
            flat_matrix.append(value)

    return flat_matrix


def make_spiral(
        layers: int,
        _matrix: Optional[List[List[int]]] = None,
        _depth: int = 0) -> List[List[int]]:

    """Returns an integer spiral with the given number of layers.

    The spiral is formed by starting with 1 in the center and moving to the
    right in a clockwise direction, incrementing the value of each subsequent
    space by 1.
    """

    # compute the dimension of one side of the spiral
    side = layers * 2 - 1

    # initialize the matrix that will hold the spiral
    if _matrix is None:
        _matrix = [[1 for _ in range(side)] for _ in range(side)]

    # base case: a spiral with one layer will contain the number 1
    if layers < 2:
        return _matrix

    side_min_1 = side - 1
    value = side * side

    # fill the top row of the spiral
    for i in range(side_min_1):
        _matrix[_depth][-1 - _depth - i] = value
        value -= 1

    # fill the left column of the spiral
    for i in range(side_min_1):
        _matrix[_depth + i][_depth] = value
        value -= 1

    # fill the bottom row of the spiral
    for i in range(side_min_1):
        _matrix[-1 - _depth][_depth + i] = value
        value -= 1

    # fill the right column of the spiral
    for i in range(side_min_1):
        _matrix[-1 - _depth - i][-1 - _depth] = value
        value -= 1

    # recurse to fill the inside of the spiral
    return make_spiral(layers - 1, _matrix, _depth + 1)


def max_bipartite_matching(edge_matrix: List[List[bool]]) -> Sequence[Coord]:
    """Returns the list of edges in the maximum matching of a bipartite graph.

    The argument edge_matrix is a boolean matrix mapping vertices in partition
    V to those in partition U, such that edge_matrix[u][v] = True iff there
    exists an edge between u and v, where u is the index of a vertex in U and v
    is the index of a vertex in V.

    Edges are returned in the format (u, v), with u and v defined as above.
    """

    n = len(edge_matrix)  # number of rows
    m = len(edge_matrix[0])  # number of columns

    # try to assign each row to a column
    col_assignments: List[int] = [-1] * m
    for i in range(n):
        col_marked = [False] * m
        _try_bipartite_match(edge_matrix, i, col_marked, col_assignments)

    # convert to list of matched pairs and return
    return [(i, j) for j, i in enumerate(col_assignments) if i != -1]


def minimum_line_cover(matrix: List[List[int]]) -> Sequence[Tuple[bool, int]]:
    """Returns a list of the fewest lines needed to cover all zeros in matrix.

    Lines are given in the format (is_vertical, i), where is_vertical is a
    boolean indicating whether the line is oriented vertically, and i is the
    index of the row (if is_vertical = False) or column (if is_vertical = True)
    in the matrix that would be covered by this line.
    """

    # assign as many (row, col) pairs with zeros as possible
    assignments = _try_assign_zeros(matrix)

    # if all zeros assigned, n lines are needed
    n = len(matrix)
    if len(assignments) == n:
        return [(False, i) for i in range(n)]

    # convert to row assignment array
    row_assignments: List[Optional[int]] = [None] * n
    for i, j in assignments:
        row_assignments[i] = j

    # mark all unassigned rows
    m = len(matrix[0])
    row_marked = [False] * n
    col_marked = [False] * m
    new_marked_rows = []
    for i, assigned_col in enumerate(row_assignments):
        if assigned_col is None:
            row_marked[i] = True
            new_marked_rows.append(i)

    while new_marked_rows:
        # mark all unmarked columns with zeros in newly marked rows
        for i in new_marked_rows:
            for j in range(m):
                if not col_marked[j] and matrix[i][j] == 0:
                    col_marked[j] = True

        # mark all unmarked rows with assigned zeros in marked columns
        new_marked_rows = []
        for i in range(n):
            if not row_marked[i]:
                assignment = row_assignments[i]
                assert assignment is not None
                if col_marked[assignment]:
                    row_marked[i] = True
                    new_marked_rows.append(i)

    # cover all unmarked rows and marked columns
    lines = []
    for i, marked in enumerate(row_marked):
        if not marked:
            lines.append((False, i))
    for j, marked in enumerate(col_marked):
        if marked:
            lines.append((True, j))

    return lines


def optimal_assignment(cost_matrix: List[List[int]]) -> Sequence[Coord]:
    """Assigns each row to a column of the square matrix cost_matrix so that
    the sum of the cost values in the assigned positions is minimized.

    Returns a list of matrix coordinates in the format (row, col).
    """

    # make a deep copy so we don't change the input matrix
    cost_matrix = copy.deepcopy(cost_matrix)

    # Step 1: subtract the minimum element from each row
    n = len(cost_matrix)
    for i, row in enumerate(cost_matrix):
        min_element = min(row)
        for j in range(n):
            cost_matrix[i][j] -= min_element

    # Step 2: subtract the minimum element from each column
    for j in range(n):
        col = [cost_matrix[i][j] for i in range(n)]
        min_element = min(col)
        for i in range(n):
            cost_matrix[i][j] -= min_element

    # Step 3: cover zeros with minimum number of lines
    lines = minimum_line_cover(cost_matrix)

    # Step 4: subtract min uncovered from all uncovered & add to double-covered
    while len(lines) < n:
        # find rows and columns covered by lines
        covered_rows = set()
        covered_cols = set()
        for is_vertical, index in lines:
            if is_vertical:
                covered_cols.add(index)
            else:
                covered_rows.add(index)

        # search for min uncovered value
        min_uncovered = None
        for i, row in enumerate(cost_matrix):
            if i in covered_rows:
                continue
            for j, value in enumerate(row):
                if j in covered_cols:
                    continue
                if min_uncovered is None or value < min_uncovered:
                    min_uncovered = value

        assert min_uncovered is not None

        # subtract and add min value to matrix entries as needed
        for i in range(n):
            for j in range(n):
                if i not in covered_rows and j not in covered_cols:
                    cost_matrix[i][j] -= min_uncovered
                elif i in covered_rows and j in covered_cols:
                    cost_matrix[i][j] += min_uncovered

        # repeat steps 3-4 until n lines are needed to cover zeros
        lines = minimum_line_cover(cost_matrix)

    # now that a total assignment exists, find and return it
    return _try_assign_zeros(cost_matrix)
