import math 

N = int(input())
log_N = math.log2(N)
max_2 = math.ceil(log_N)
sum_abc = math.inf
for i in range(max_2+1):
    b = i
    a = N // 2 ** b
    c = N - a* 2 ** b
    if a+b+c < sum_abc:
        sum_abc = a+b+c
print(sum_abc)