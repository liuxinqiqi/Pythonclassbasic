#!/usr/bin/python
#coding=utf-8
# l = [[5,2,7,3],[4,9,2,8],[5,1,6,7]]
    # outLen = len(l)
    # inLen = len(l[0])
#
# for i in l:
#     for j in i:
#         print j,
#     print ""

# 最大值及位置
# i = j = 0
# x = y = 0
# max = l[0][0]
#
# while i < outLen:
#     j = 0
#     while j < inLen:
#         if l[i][j] > max:
#             max = l[i][j]
#             x,y = i,j
#
#         j += 1
#     i += 1
#
# print "l[%d][%d] = %d"%(x,y,max)

# 鞍点
# for i in l:
#     m = max(i)
#     n = i.index(m)
#     j = 0
#     while j < len(l):
#         if l[j][n] > m:
#             break
#         j += 1
#     else:
#         print i[n]

#杨辉三角

l = []

for i in range(15):
    l.append([])
    l[i].append(1)
    for j in range(1,i + 1):
        l[i].append(l[i - 1][j - 1] + l[i - 1][j])
    l[i].append(0)

for i in l:
    i.pop()
    print i
