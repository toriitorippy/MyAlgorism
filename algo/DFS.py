#深さ優先探索
#copy from https://atcoder.jp/contests/atc001/submissions/6045503

import sys
sys.setrecursionlimit(300000)
 
H, W = map(int, input().strip().split())
c = []
for i in range(H):
    temp = list(input())
    if temp.count('s'):
        s = (i, temp.index('s'))
    c.append(temp)
 
def dfs(c, n):
    x, y = n
    if not(0<=x<=H-1) or not(0<=y<=W-1) or c[x][y]=="#":
        return False
    if c[x][y]=="g":
        return True
    c[x][y] = "#"
    return dfs(c, (x-1, y)) or dfs(c, (x+1, y)) or dfs(c, (x, y-1)) or dfs(c, (x, y+1))
 
if dfs(c, s):
    print('Yes')
else:
    print('No')