# https://github.com/vampirevilage/100DaysOfCode.git
import math
def isPalindrome(n):
    if(n==int(str(n)[::-1])):
        return True
    else:
        return False

def maxPalindromeProduct(n):
    maxPalProd = -1
    lower_limit = 100
    upper_limit = 1000
    for i in range(lower_limit, upper_limit):
        for j in range(100000//i + 1, upper_limit):
            if(i%11==0 or j%11==0):
                product = i*j
            else:
                break
            if(product <= maxPalProd):
                break
            if(product>=n):
                break
            if(isPalindrome(product)):
                maxPalProd=product
    return maxPalProd

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(maxPalindromeProduct(n))

