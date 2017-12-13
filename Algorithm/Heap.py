#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果一颗完全二叉树中, 每个父节点的值都大于等于(或者都小于等于)其左右子节点的值, 这样的完全二叉树称为堆.
# 此处以一个小根堆为例(即父节点的值小于等于左右子节点的值)

# 堆的插入, 弹出(删除根节点), 以及利用堆进行排序


class Heap(object):

    def __init__(self):
        self.data = []

    def swap(self, indexA, indexB):
        y = self.data[indexA]
        self.data[indexA] = self.data[indexB]
        self.data[indexB] = y

    def add(self, value):
        self.data.append(value)
        # 上浮
        c = len(self.data) - 1
        p = (c - 1) // 2
        while self.data[p] > self.data[c]: # 大根堆此处为<
            self.swap(c, p)
            c = p
            p = (p - 1) // 2

    def pop(self):
        self.swap(0, len(self.data) - 1)
        value = self.data.pop()
        length = len(self.data)
        # 下沉
        p = 0
        while (p * 2 + 1) < length:
            c = p * 2 + 1
            if ((p * 2 + 2) < length) and (self.data[p * 2 + 1] > self.data[p * 2 + 2]): # 大根堆此处为<
                c = p * 2 + 2
            if self.data[p] > self.data[c]: # 大根堆此处为<
                self.swap(p, c)
                p = c
            else:
                break
        return value


def heapSort(l):
    heap = Heap()
    for i in l:
        heap.add(i)
    for i in l:
        print(heap.pop(), end=" ")

heapSort([1,4,3,2,7,5,6,9,3])



