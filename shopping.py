#! /usr/bin/env python3
# coding=utf-8
def DP(n,W):#a DP function to find the max value
    v=[0 for x in range(W+1)]
    for i in range(n):
        for j in range(W+1):
            if W-j>=weight[i]:
                a=v[W-j]
                b=v[W-j-weight[i]]+value[i]
                v[W-j]=max(a,b)
    return v[-1]

f = open("shopping.txt", "r")
testcase = int(f.readline().strip())
outFile = open("result.txt", "w")
for x in range(testcase):
    n = int(f.readline().strip())
    weight=[]# create a empty array
    value=[]# create a empty array
    for i in range(n):
        p,W=map(int, f.readline().strip().split())
        weight.append(W)# the weights of the items
        value.append(p)# the price of the items
    F=int(f.readline().strip())
    F_weight=[]
    for i in range(F):
        F_weight.append(int(f.readline().strip()))# the weight that each person can take
        for W in F_weight:
            value_1=DP(n,W)
    outFile.write("Testcase:%d" %(x+1))
    outFile.write("Total price:%d"%value_1)
    for i in range(F):
        outFile.write("Member items:%d"%(F+1))

        
