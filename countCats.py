# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:46:25 2017

@author: arnab
"""

from collections import Counter
import math
if __name__ == '__main__':
	arr = map(int, raw_input().strip().split(","))
	c = Counter(arr)
	total = 0
	for key in c:
		total += int(math.ceil(float(c[key])/(key+1))) * (key+1)
	print (total)
