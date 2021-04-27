N, Q = map(int, input().split()) 
S = input()
s_list = [0]*(N)
for i in range(1,N):
  if S[i-1] == "A" and S[i] == "C":
    s_list[i] = s_list[i-1] + 1
  else:
    s_list[i] = s_list[i-1]

for _ in range(Q):
  l,r = map(int, input().split())
  print(s_list[r-1]-s_list[l-1])