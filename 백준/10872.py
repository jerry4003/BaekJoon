def factorial(A):
    if A==0:
        return 1
    elif A==1:
        return 1
    else:
        return A*factorial(A-1)
N=int(input())
print(factorial(N))
