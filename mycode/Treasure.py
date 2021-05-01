# https://atcoder.jp/contests/abc035/tasks/abc035_d

#　価値が高い町にずっといたほうが良い
# それぞれの町への最短時間を求めて各町に辿り着いた時の所持金を考える

from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

def back_dijkstra(s, n): #(終点、ノード数)
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

def value(d,A,T):
    value_list = [0]*len(d)
    for i in range(len(d)):
        time = T - 2*d[i]
        print(time)
        if time > 0:
            value_list[i] = time*A[i]
    return value_list


def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    global adj
    adj = [[] for _ in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((b,c))
    d = dijkstra(0,N)
    print(max(value(d,A,T)))

if(__name__ == '__main__'):
    main()