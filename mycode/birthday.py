N, K = map(int, input().split())
# 合計がMの個数を考える
#(1,1,M-2)など
#M+2の組み合わせ
count = 0
M = 3
while True:
    new_count = count + (M-2)*(M-1)*M / 6
    if new_count >=K:
        break
    M += 1
    count = new_count

amari = K - count
#合計がM+1の配列のamari番目
#一番目は(1,1,M-1)

M = M+1
p = 0
tmp_M = M
print(count,M)
for i in range(N):
  if not tmp_M <= N:
    new_p = p + tmp_M * (tmp_M-1) //2
    if new_p >= amari:
        break
    else:
        p = new_p
  tmp_M -= 1
i = i+1
tmp_M = tmp_M - i -1
for j in range(N):
  if not tmp_M <= N:
    new_p = p + tmp_M
    if new_p >= amari:
        break
    else:
        p = new_p
  tmp_M -= 1
j = j + 1   
k = M -i-j
print(i,j,k)