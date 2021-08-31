import sys

A,B,C=map(int,sys.stdin.readline().split())
R=A%C
def mul(R,B):
    if B==1:
        return R%C
    else:
        K=mul(R,B//2)
        if B%2==0:
            return K*K%C
        else:
            return K*K*R%C
print(mul(R,B))