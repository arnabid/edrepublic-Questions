# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:46:57 2017

@author: arnab
"""

import itertools
import math
from collections import Counter

def check(item, magicSum):
	if sum(item[0:3]) != magicSum:
		return False
	if sum(item[3:6]) != magicSum:
		return False
	if sum(item[6:9]) != magicSum:
		return False
	if sum(item[0:9:3]) != magicSum:
		return False
	if sum(item[1:9:3]) != magicSum:
		return False
	if sum(item[2:9:3]) != magicSum:
		return False
	return True

if __name__ == '__main__':
	arr = map(int, raw_input().strip().split(","))
	total = sum(arr)
	
	if total % 3 != 0:
		print (0)
	else:
		c = Counter(arr)
		f = 1
		for key in c:
			if c[key] > 1:
				f *= math.factorial(c[key])
			
		magicSum = total / 3
		perms = list(itertools.permutations(arr))
		count = 0
		for item in perms:
			if check(item, magicSum):
				count += 1
		print (count/f)
