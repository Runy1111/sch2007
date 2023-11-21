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


print(gis(int(input()), list(map(int, input().split()))))
