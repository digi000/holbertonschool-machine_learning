#!/usr/bin/env python3
"""Author: Jordan Tuyisenge"""
import numpy as np

def np_cat(mat1, mat2, axis=0):
    """Concatenates two numpy.ndarrays along a specific axis"""
    return np.concatenate((mat1, mat2), axis=axis)
