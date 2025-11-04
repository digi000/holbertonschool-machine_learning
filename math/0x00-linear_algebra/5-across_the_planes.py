#!/usr/bin/env python3
"""
author: Jordan Tuyisenge
"""

def add_matrices2D(mat1, mat2):
    """
    adds two matrices element-wise
    """
    if len(mat1) != len(mat2) or len(mat1[1]) != len(mat2[1]):
        return None
    added = []
    for i in range(len(mat1)):
        radd = []
        for j in range(len(mat1[1])):
            radd.append(mat1[i][j] + mat2[i][j])
        added.append(radd)
    return added
