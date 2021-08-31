import sys
result=[0]*100
def p(case):
    if case==1 or case==2 or case==3:
        return 1
    if result[case-1]:
        return result[case-1]
    result[case-1]= p(case-3)+p(case-2)
    return result[case-1]
T=int(sys.stdin.readline())
for _ in range(T):
    case=int(sys.stdin.readline())
    print(p(case))