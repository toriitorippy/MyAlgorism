# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from heapq import heappush, heappop

def is_top(map_list,i,j):
    if map_list[i][j] > map_list[i-1][j] and map_list[i][j] > map_list[i][j-1] and map_list[i][j] > map_list[i+1][j] and map_list[i][j] > map_list[i][j+1]:
        return True
    else:
        return False

N = int(input())
map_list = []
tmp = [0]*(N+2)
map_list.append(tmp)
for _ in range(N):
    new_list = [0] + list(map(int, input().split())) + [0]
    map_list.append(new_list)
map_list.append(tmp)

top_heap = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if is_top(map_list,i,j):
            heappush(top_heap,-map_list[i][j])


for i in range(len(top_heap)):
    ans = -heappop(top_heap)
    print(ans)



