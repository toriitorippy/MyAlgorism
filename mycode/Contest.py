N = int(input())
A = list(map(int, input().split()))

#メモ化再帰
W = sum(A)
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for w in range(W+1):
        if dp[i][w] == 1:
            dp[i+1][w] = 1
        if w + A[i] <= W:
            dp[i+1][w + A[i]] = max(dp[i+1][w+A[i]], dp[i][w])

print(sum(dp[N]))