#!/usr/bin/env python3
"""
Author: Jordan Tuyisenge
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Returns a new matrix or None if dimensions are incompatible.
    """
    if not mat1 or not mat2:
        return None

    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])

    if axis == 0:
        if cols1 != cols2:
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]

    if axis == 1:
        if rows1 != rows2:
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(rows1)]

    return None

