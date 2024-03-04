N = int(input())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
su = 0
for i in range(N):
    for j in range(N):
        if i <= j:
            su += a[i][j]
        elif a[i][j] != a[j][i]:
            su += a[i][j]
print(su)
