# https://atcoder.jp/contests/arc037/tasks/arc037_c

import bisect
N, K = map(int,input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

# ng = A[0] * B[0]
# ok = A[N-1] * B[N-1] * 2
ng = -1
ok = 10 ** 18 + 1


while ok - ng > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for i in range(N):
        x = mid // A[i]
        cnt += bisect.bisect_right(B,x)
    if cnt >= K:
        ok = mid
    else:
        ng = mid
print(ok)
