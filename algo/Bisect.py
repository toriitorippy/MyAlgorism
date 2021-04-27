#問題：https://atcoder.jp/contests/abc077/tasks/arc084_a
#copy from https://atcoder.jp/contests/abc077/submissions/21956556

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))
 
import bisect
ans = 0
for b in B:
    a = bisect.bisect_left(A, b)
    c = N - bisect.bisect_right(C, b)
 
    ans += a * c
 
print(ans)