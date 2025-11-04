#!/usr/bin/env python3
"""define matrix shape"""
def matrix_shape(matrix):
    """calculates the shape of a matrix"""
    shape = []
    depth = len(matrix)
    shape.append(depth)
    if isinstance(matrix[1], list):
        rows = len(matrix[1])
        shape.append(rows)
        if isinstance(matrix[1][1], list):
            cols = len(matrix[1][1])
            shape.append(cols)
    return shape
