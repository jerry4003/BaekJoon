import sys
N,K=map(int,sys.stdin.readline().split())
from math import factorial
result = factorial(N) // ((factorial(K) * factorial(N-K)))
print(result % 10007)