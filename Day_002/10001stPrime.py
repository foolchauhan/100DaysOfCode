import math
isPrime = []
primes = []
def SieveOfEratosthenes():
    for i in range(1000005):
        isPrime.append(True)
    
    for p in range(2, int(math.sqrt(1000005))):
        if(isPrime[p]):
            for q in range(p*p, 1000005, p):
                isPrime[q] = False
    
    for z in range(2, 1000005):
        if(isPrime[z]):
            primes.append(z)
    
if __name__ == '__main__':
    SieveOfEratosthenes()
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(primes[n-1])
        