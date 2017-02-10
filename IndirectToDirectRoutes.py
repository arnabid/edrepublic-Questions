# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:43:46 2017

@author: arnab
"""

from collections import Counter

def getCount(graph, node):
	visited = Counter()
	visited[node] = True
	count = [0]
	def dfs(v):
		for w in graph[v]:
			if not visited.get(w, False):
				count[0] += 1
				visited[w] = True
				if w in graph:
					dfs(w)
	dfs(node)
	return count[0]

if __name__ == '__main__':
	n = int(raw_input())
	graph = Counter()
	for i in xrange(n):
		graph[i] = map(int, raw_input().strip().split(","))

	total = 0
	for node in graph:
		total += getCount(graph, node)
	print (total)
