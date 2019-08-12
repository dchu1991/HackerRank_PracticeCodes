# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:51:16 2019

@author: user
"""

def maxSubsetSum(arr):
    LEN = len(arr)
    cache = {}
    cache[0] = max(0,arr[0])
    cache[1] = max(cache[0],arr[1])

    for i in range(2,LEN):
        cache[i] = max(cache[i-1],cache[i-2]+arr[i])

    return cache[LEN-1]