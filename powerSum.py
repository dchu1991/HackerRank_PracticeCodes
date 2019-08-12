# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:27:40 2019

@author: user
"""

def powerSum(X, N, num = 1):

    if pow(num,N) < X:
        return powerSum(X-pow(num,N), N, num = num+1) + \
               powerSum(X, N, num = num+1)
    elif pow(num,N) == X:
        return 1
    else:
        return 0
        
        