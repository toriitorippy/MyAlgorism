N = int(input())
S = list(input())
T = list(input())

a = []
b = []
for i in range(N):
    if S[i] == "0":
        a.append(i)
    if T[i] == "0":
        b.append(i)
if not len(a) == len(b):
    print(-1)
else:
    ans = 0
    for i in range(len(a)):
        if not a[i] == b[i]:
            ans += 1
    print(ans)
