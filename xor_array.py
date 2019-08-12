# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:13:06 2019

@author: user
"""
from functools import lru_cache

@lru_cache(maxsize = 1000)
def gen_array_ele(n):
    if n == 0:
        return 0
    else:
        return gen_array_ele(n-1)^n
    