# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:50:06 2017

@author: arnab
"""

from collections import Counter
from fractions import gcd
import Queue

def lcm(a, b):
    return (a * b) // gcd(a, b)

if __name__ == '__main__':
    n = int(raw_input())
    nodes = {}
    nodes[0] = (1,1)
    
    graph = Counter()
    for i in xrange(n):
        graph[i] = {}
    
    for _ in xrange(n-1):
        s = raw_input().strip().split(" ")
        x,y = int(s[0][1:]), int(s[2][1:])
        wts = s[4].split(":")
        w1,w2 = int(wts[0]), int(wts[1])
        gd = gcd(w1,w2)
        w1 = w1//gd
        w2 = w2//gd
        
        graph[x][y] = w1
        graph[y][x] = w2
    
    # start the bfs from node 0
    q = Queue.Queue()
    q.put(0)
    marked = Counter()
    marked[0] = True
    
    while not q.empty():
        v = q.get()
        
        for w in graph[v]:
            if not marked.get(w, False):
                num = nodes[v][0] * graph[v][w]
                den = nodes[v][1] * graph[w][v]
            
                nodes[w] = (num, den)
                marked[w] = True
                q.put(w)
    
    l = 1
    for node in xrange(n):
        l = lcm(l, nodes[node][0])

    masses = [l]
    for node in xrange(1,n):
        masses.append(l*nodes[node][1]//nodes[node][0])

    gd = 0
    for i in xrange(n):
        gd = gcd(gd, masses[i])
    for i in xrange(n):
        masses[i] = masses[i]//gd
        print (masses[i])
