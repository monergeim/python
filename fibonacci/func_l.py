#!/usr/bin/python3.8

#calculates the nth Fibonacci number in O(n) time == without using any "for" or "while" loops

import numpy as np

num = input("Enter fibonacci num:")

def fib_matrix(n):
    Matrix = np.matrix([[0,1],[1,1]])
    vec = np.array([[0],[1]])
    F=np.matmul(Matrix**n,vec)
    return F[0,0]

print("Fibonacci n-th number is: " + str(fib_matrix(int(num))))
