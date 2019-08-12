# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:45:19 2019

@author: user
"""
# =============================================================================
# import math
# import os
# import random
# import re
# import sys
# 
# =============================================================================
def staircase(n):
    A = stairblock(n)
    for i in range(n):
        print(A[i])

def stairblock(n):
    
    stair = '#'
    result = []

    if n == 1:
        result.append(stair)
        return result
    else:
        string = ''
        for i in range(n):
            string += stair
        result = buildingstair(n-1,staircase(n-1))
        result.append(string)
        return result
        
def buildingstair(n,res):
    space = ' '

    for i in range(n):
        res[i] = space + res[i]

    return res
  
if __name__ == '__main__':
    staircase(3)