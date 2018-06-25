#!/usr/bin/python

from scipy.linalg import svd

matrix = [[1,0,1,0,0,0],
[0,1,0,0,0,0],
[1,1,0,0,0,0],
[1,0,0,1,1,0],
[0,0,0,1,0,1]]

U, S, Vt = svd(matrix)

print U
print S
print Vt