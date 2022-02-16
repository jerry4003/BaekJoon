import sys
from itertools import combinations
N=int(sys.stdin.readline())
number=[]
for _ in range(N):
    number.append(list(map(int,sys.stdin.readline().split())))
possible_team=[]
possible_team_member=[i for i in range(N)]
possible_team=list(combinations(possible_team_member,N//2))
min_size=sys.maxsize
for i in range(len(possible_team)//2):
    team_start=possible_team[i]
    team_start_ability=0
    for j in team_start:
        for k in team_start:
            if j!=k:
                  team_start_ability+=number[j][k]
    team_link=possible_team[len(possible_team)-1-i]
    team_link_ability=0
    for j in team_link:
        for k in team_link:
            if j!=k:
                  team_link_ability+=number[j][k]
    min_size=min(min_size,abs(team_start_ability-team_link_ability))
print(min_size)   