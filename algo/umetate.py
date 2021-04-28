# https://atcoder.jp/contests/arc031/tasks/arc031_2
# 参考：https://atcoder.jp/contests/arc031/submissions/21981152


import sys
sys.setrecursionlimit(300000)

# 繋がっているどうかを深さ優先探索で確認


def dfs(start, map_):
    r, c = start
    n_land = 0
    stack = [start]
    is_visited = set()
    while stack:
        position = stack.pop()
        if position in is_visited:
            continue
        is_visited.add(position)
        n_land += 1
        for dh, dw in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            r, c = position[0]+dh, position[1]+dw
            next_ = (r, c)
            if next_ in is_visited or not(0 <= r < 10) or not(0 <= c < 10) or map_[r][c] == 'x':
                continue
            stack.append(next_)
    return n_land


def main():
    size = 10
    map_ = [input() for _ in range(size)]
    n_land = sum([line.count('o') for line in map_])
    for i in range(size):
        for j in range(size):
            if map_[i][j] == 'o':
                continue
            # （i,j）を埋め立てた時に繋がっている島になっているか
            if dfs((i,j),map_) == n_land + 1:
                print("Yes")
                exit()
    print("No")

if(__name__ == '__main__'):
  main()
