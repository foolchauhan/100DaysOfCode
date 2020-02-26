# https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem
#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    z = n*(n+1)
    a = (z/2) * (z/2)
    b = (z*((2*n)+1))/6

    print(int(a - b))
