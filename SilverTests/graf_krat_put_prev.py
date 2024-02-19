def BFS():
    q = []
    ans = [end + 1]
    prev = [-1] * n
    q.append(start)
    was = [False] * n
    was[start] = True
    while len(q) != 0:
        now = q.pop(0)
        for i in graph[now]:
            if not was[i]:
                prev[i] = now
                was[i] = True
                q.append(i)
                way[i] = way[now] + 1
                if i == end:
                    k = end
                    while prev[k] != -1:
                        ans.append(prev[k] + 1)
                        k = prev[k]
                    return way[end], ans[::-1]
    return -1, -1


n = int(input())
a = []
graph = []
for i in range(n):
    graph.append([])
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] == 1:
            graph[i].append(j)
            graph[j].append(i)
start, end = map(int, input().split())
start, end = start - 1, end - 1
way = [0] * n
if start == end:
    print(0)
    print(end + 1)
else:
    x, y = BFS()
    if x == -1:
        print(-1)
    else:
        print(x)
        print(*y)
