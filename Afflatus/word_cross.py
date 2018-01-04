#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 问题来源: 由MU全队球员名构成的Manchester United
# 问题推广: 设有一个货轮, 有n个仓位, 另有m件货物, 每一个仓位可以m件货物中的一些, 问如何分配达到最优

# 目前只想到搜索的方法...


team = "Manchester United"
names = [
"MOURINHO"
, "DE GEA"
, "LINDELOF"
, "BAILLY"
, "JONES"
, "ROJO"
, "POGBA"
, "MATA"
, "LUKAKU"
, "IBRAHIMOVIC"
, "MARTIAL"
, "SMALLING"
, "LINGARD"
, "CARRICK"
, "BLIND"
, "YOUNG"
, "RASHFORD"
, "ROMERO"
, "HERRERA"
, "MKHITARYAN"
, "SHAW"
, "VALENCIA"
, "FELLAINI"
, "MATIC"
, "DARMIAN"
, "TUANZEBE"
, "MCTOMINAY"
]

#team = "MAN"
#names = ["AN", "M", "A"]

position = []
bo = [-1 for i in range(len(names))]

def pre():
    global team
    team = team.upper()
    team = team.replace(" ", "")
    for name in names:
        name = name.upper()
    for x in range(len(team)):
        l = []
        for y in range(len(names)):
            if names[y].find(team[x]) >= 0:
                # print(names[y] + " " + team[x])
                l.append(y)
        position.append(l)

maxm = 0
result = []

def work():
    def search(n, m):
        global maxm
        global result
        if m + len(position) - n < maxm:
            return
        if n == len(position):
            if m >= maxm:
                maxm = m
                result = bo[:] # copy list by value
                post()
        else:
            for x in position[n]:
                if bo[x] == -1:
                    bo[x] = n
                    search(n+1, m+1)
                    bo[x] = -1
            search(n+1, m)


    search(0, 0)
    print(maxm)
    print(result)


def post():
    global team
    lines = list(team)
    maxLineLength = 0
    for i in range(len(result)):
        if result[i] != -1:
            lines[result[i]] = names[i]
        if len(names[i]) > maxLineLength:
            maxLineLength = len(names[i])
    for i in range(len(lines)):
        print(" "*(2*maxLineLength-lines[i].find(team[i])) + lines[i])
    print()

pre()
work()
post()