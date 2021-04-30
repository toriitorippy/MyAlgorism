# 参考解説：https://atcoder.jp/contests/tdpc/editorial/757
A, B= map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 最高点が取れるような行動をする
# dpは（先手が得る価値) - (後手が得る価値)
dp = [[0 for _ in range(B+1)] for _ in range(A+1)]
dp[0][0] = 0

# Aだけの初期値
for i in range(1,A+1):
    dp[i][0] = a[A-i] - dp[i-1][0]

for j in range(1,B+1):
    dp[0][j] = b[B-j] - dp[0][j-1]

for i in range(1,A+1):
    for j in range(1,B+1):
        dp[i][j] = max(a[A-i] - dp[i-1][j], b[B-j] - dp[i][j-1])

print(int((dp[A][B] + sum(a) + sum(b))/2))

