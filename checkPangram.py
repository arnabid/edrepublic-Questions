# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:33:05 2017

@author: arnab
"""
from collections import Counter

if __name__ == '__main__':
    s = raw_input().strip()
    c = Counter(s)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    ans = ''
    for letter in alphabet:
    	if letter not in c and letter.lower() not in c:
    		ans += letter
    if ans == '':
    	ans = '-'
    print (ans)