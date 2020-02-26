# https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=1
    for k in (range(1, n+1)): 
        if i % k > 0: 
            for j in range(1, n+1): 
                if (i*j) % k == 0: 
                    i *= j 
                    break 
    print (i)
