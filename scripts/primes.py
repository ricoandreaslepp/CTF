import sys

def isprime(n):
    for i in range(2, int(pow(n, 1/2))+1):
        if n%i==0:
            return False
    return True

if len(sys.argv) < 2:
    print("usage: python primes.py <PRIMES_UNDER_NUMBER>")
    sys.exit(0)
    
primes = list(filter(lambda x: isprime(x), list(i for i in range(2, int(sys.argv[1])))))
print(*primes)
