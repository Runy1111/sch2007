def dfs(start):
    for i in v[start]:
        if was[i] != 1:
            return dfs(i)
        else:
            return True
    return False


n = int(input())
v = [set() for i in range(n)]
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            v[i].add(j)
was = [0] * n
ans = 0
for i in range(n):
    was[i] = 1
    if dfs(i):
        ans = 1
        break
    was[i] = 2
print(ans)
