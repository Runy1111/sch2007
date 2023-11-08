len_1 = int(input())
mas_1 = list(map(int, input().split()))
len_2 = int(input())
mas_2 = list(map(int, input().split()))

cash = [[0] * (len_1 + 1)]
for i in range(len_2):
    cash.append([0] * (len_1 + 1))
prev = []

for i in range(1, len_2 + 1):
    for j in range(1, len_1 + 1):
        if mas_1[j-1] == mas_2[i-1]:
            cash[i][j] = cash[i-1][j-1] + 1
        else:
            cash[i][j] = max(cash[i-1][j], cash[i][j-1])

while cash[i][j] != 0:
    if mas_1[j-1] != mas_2[i-1]:
        if cash[i-1][j] > cash[i][j-1]:
            i -= 1
        else:
            j -= 1
    else:
        prev.append(mas_1[j-1])
        i -= 1
        j -= 1
print(*prev[::-1])
