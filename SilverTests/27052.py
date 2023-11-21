def gis(n, sub):
    inf = max([abs(elem) for elem in sub]) + 1
    ans = []
    prev = [-inf] * (n + 1)
    pos = [-inf] * (n + 1)
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
        pos[right] = i
        prev[i] = pos[right - 1]
    i = n + 1
    while F[i] == inf:
        i -= 1
    long = i
    i = pos[i]
    while i != -inf:
        ans.append(sub[i])
        i = prev[i]
    return long, ans[::-1]


a, b = gis(int(input()), list(map(int, input().split())))
print(a)
print(*b)

