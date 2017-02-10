# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:48:59 2017

@author: arnab
"""

import itertools

def isClassicWord(s, m):
    count = 0
    k = len(s)
    doubles = s + s
    for i in range(k):
        if doubles[i:i+k] == s:
            count += 1
    return count == m
    

if __name__ == '__main__':
    Q = raw_input().strip().split(",")
    perm_strings = itertools.permutations(Q)
    
    m = int(raw_input())

    ans = 0
    classics = set()
    # generate all the permuted strings
    for item in perm_strings:
        temp = ''
        for sub in item:
            temp += sub
        if temp in classics:
            ans += 1
        else:
            if isClassicWord(temp, m):
                ans += 1
                classics.add(temp)
    print (ans)
