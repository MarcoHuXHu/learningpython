#!/usr/bin/env python3
# -*- coding: utf-8 -*-

parent = []

def find_root(n):
    if parent[n] == n:
        return n
    else:
        root = find_root(parent[n])
        parent[n] = root
        return root

def merge(a,b):
    parent[find_root(b)] = find_root(a)

def init(n):
    for x in range(n+1):
        parent.append(x)

