#!/usr/bin/env python3
"""
Author: Jordan Tuyisenge
"""
def cat_arrays(arr1, arr2):
    """concatenates two arrays"""
    re_arr = arr1.copy()
    for i in range(len(arr2)):
        re_arr.append(arr2[i])
    return re_arr
