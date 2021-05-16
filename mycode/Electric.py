import sys
import math
import copy
sys.setrecursionlimit(300000)

N = int(input())
S = list(input())
T = list(input())
S = [int(x) for x in S]
T = [int(x) for x in T]


def check_first_rule(l,r,S):
    flg = True
    if not S[l] == 0:
        flg = False
    for i in range(l+1,r):
        if not S[i] == 1:
            flg = False
            break
    return flg

def check_second_rule(l,r,S):
    flg = True
    for i in range(l,r-1):
        if not S[i] == 1:
            flg = False
            break
    if not S[r] == 0:
        flg = False
    return flg

def dfs(S,count,min_count,pattern_list):
    pattern_list.append(S)
    for l in range(len(S)):
        for r in range(l+1, len(S)):
            # print(S, l,r,check_second_rule(l,r,S))
            if check_first_rule(l,r,S):
                new_S = copy.copy(S)
                tmp = new_S[l]
                new_S[l] = new_S[r]
                new_S[r] = tmp
                if new_S == T:
                    if count <= min_count:
                        min_count = count
                elif not new_S in pattern_list:
                    min_count = dfs(new_S,count+1,min_count,pattern_list)
            if check_second_rule(l,r,S):
                new_S = copy.copy(S)
                tmp = new_S[l]
                new_S[l] = new_S[r]
                new_S[r] = tmp
                if new_S == T:
                    if count <= min_count:
                        min_count = count
                if not new_S in pattern_list:
                    min_count = dfs(new_S,count+1,min_count,pattern_list)
    return min_count

pattern_list = []
if S ==T:
    print(0)
elif not sum(S) == sum(T):
    print(-1) 
else:
    min_count = dfs(S,0, math.inf,pattern_list)
    if min_count == math.inf:
        print(-1)
    else:
        print(min_count)