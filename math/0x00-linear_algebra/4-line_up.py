#!/usr/bin/env python3
"""
@author: Jordan Tuyisnge
"""

def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    added = []
    for i in range(len(arr1)):
        added.append(arr1[i] + arr2[i])
    return added
