#!/usr/bin/env python3

"""Common library for working with numerical vectors and matrices.

This module provides functions for operating one-dimensional sequences
(vectors) and two-dimensional collections (matrices) of numbers. Examples
include calculating dot and cross products and finding the optimal assignment
in a cost matrix.
"""

import copy
from typing import Iterable, List, Optional, Sequence, Tuple

from common.typex import Coord, Matrix, T


def _try_assign_zeros(matrix: Matrix[int]) -> Sequence[Coord]:
    """Finds the most zeros possible in distinct rows and columns of a matrix.

    Args:
        matrix: A two-dimensional integer matrix.

    Returns:
        A sequence of integer tuples, each representing the row and column of a
        zero value in ``matrix``, no two of which share the same row or column.
    """
    # convert matrix to bipartite graph, with zeros indicating edges
    edge_matrix = [[value == 0 for value in row] for row in matrix]
    return max_bipartite_matching(edge_matrix)

def _try_bipartite_match(
    edge_matrix: Matrix[bool],
    row: int,
    col_marked: List[bool],
    col_assignments: List[int],
) -> bool:
    """Tries to assign a free column to a matrix row, reassigning as necessary.

    Args:
        edge_matrix: A boolean matrix indicating edges between rows and
            columns. In order for column ``j`` to be assigned to row ``i``,
            ``edge_matrix[i][j]`` must be ``True``.
        row: Index of the row to be assigned a free column.
        col_marked: Aist of columns pending assignment in the current recursive
            call stack.
        col_assignments: An integer list of length ``len(edge_matrix[0])``,
            where the value at each index ``i`` is the index of the column
            assigned to row ``i``, or -1 if row ``i`` has no assigned column.

    Returns:
        ``True`` if ``row`` was successfully assigned a free column, possibly
        by reassigning columns to other rows in ``col_assignments``, or
        ``False`` otherwise.
    """

    # try to match row to each column
    for j in range(len(edge_matrix[0])):

        # check if row can be matched with unmarked column
        if edge_matrix[row][j] and not col_marked[j]:
            col_marked[j] = True

            # check if column is unmatched or can be re-matched with new row
            if (
                col_assignments[j] == -1 or
                _try_bipartite_match(
                    edge_matrix,
                    col_assignments[j],
                    col_marked,
                    col_assignments,
                )
            ):
                col_assignments[j] = row
                return True

    # couldn't match row with any column
    return False


def cross_product_3d(
    p1: Sequence[float],
    p2: Sequence[float],
) -> Tuple[float, float, float]:
    """Returns the cross product of two 3-dimensional points.

    Args:
        p1: A sequence of length 3, representing the coordinates of a 3D point.
        p2: A second sequence of length 3, representing another 3D point.

    Returns:
        A tuple of three numbers, representing the cross product ``p1 x p2`` of
        the two original points.
    """

    # compute determinant of cross product matrix
    prod_i = (p1[1] * p2[2]) - (p1[2] * p2[1])
    prod_j = (p1[2] * p2[0]) - (p1[0] * p2[2])
    prod_k = (p1[0] * p2[1]) - (p1[1] * p2[0])

    return prod_i, prod_j, prod_k


def dot_product(u: Iterable[float], v: Iterable[float]) -> float:
    """Returns the dot product of vectors u and v."""
    return sum(i * j for i, j in zip(u, v))


def flatten_matrix(matrix: Matrix[T]) -> Sequence[T]:
    """Builds a sequence from the elements of a matrix, in row-major order.

    Args:
        matrix: A two-dimensional matrix of values.

    Returns:
        A one-dimensional sequence of values taken from ``matrix``.
        Specifically, if ``matrix`` has ``n`` rows and ``m`` columns, the
        resulting sequence will have the form::

            [
                matrix[0][0], matrix[0][1], ..., matrix[0][m - 1],
                matrix[1][0], matrix[1][1], ..., matrix[1][m - 1],
                ...,
                matrix[n - 1][0], matrix[n - 1][1], ..., matrix[n - 1][m - 1]
            ]
    """
    flat_matrix: List[T] = []
    for row in matrix:
        for value in row:
            flat_matrix.append(value)
    return flat_matrix


def make_spiral(
    layers: int,
    _matrix: Optional[Matrix[int]] = None,
    _depth: int = 0
) -> Matrix[int]:
    """Constructs an integer spiral with a given number of layers.

    Args:
        layers: A positive integer number of layers.

    Returns:
        A spiral matrix formed by starting with 1 in the center and moving to
        the right in a clockwise direction, incrementing the value of each
        subsequent space by 1. The resulting matrix will have
        ``layers * 2 - 1`` rows and columns.
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


def max_bipartite_matching(edge_matrix: Matrix[bool]) -> Sequence[Coord]:
    """Finds the edges in the maximum matching of a bipartite graph.

    Args:
        edge_matrix: A boolean matrix mapping vertices in partition ``V`` to
        those in partition ``U``. ``edge_matrix[u][v]`` must be ``True`` if and
        only if there is an edge between ``u`` and ``v``, where ``u`` is the
        index of a vertex in ``U`` and ``v`` is the index of a vertex in ``V``.

    Returns:
        A sequence of matrix coordinates in the maximum matching of the
        bipartite graph ``U + V``. Each coordinate is of the form ``(u, v)``,
        with ``u`` and ``v`` defined as above.
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


def minimum_line_cover(matrix: Matrix[int]) -> Sequence[Tuple[bool, int]]:
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


def optimal_assignment(cost_matrix: Matrix[int]) -> Sequence[Coord]:
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
