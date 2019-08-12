# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:10:21 2019

@author: user
"""

def powerset(arr):
    LEN = len(arr)
    res = []
    for i in range(1 << LEN):
        res.append([arr[j] for j in range(LEN) if (i & (1 << j))])
    return res