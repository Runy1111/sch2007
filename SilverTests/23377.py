def gis(n, sub):
    inf = max([abs(elem) for elem in sub]) + 1
    F = [-inf] + [inf] * (n+1)
    for i in range(n):
        left = 0
        right = n + 1
        while left + 1 < right:
            middle = (left + right) // 2
            if F[middle] < sub[i]:
                left = middle
            else:
                right = middle
        F[right] = sub[i]
    i = n + 1
    while F[i] == inf:
        i -= 1
    return i


size = int(input())
num = list(map(int, input().split()))
k = int(input())
ans = []
for j in range(k):
    f, s = map(int, input().split())
    ans.append(gis(s - f + 1, num[f-1:s]))
for j in ans:
    print(j)
