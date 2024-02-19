def BFS():
    q = []
    q.append(start)
    was = [False] * n
    was[start] = True
    while len(q) != 0:
        now = q.pop(0)
        for i in graph[now]:
            if not was[i]:
                was[i] = True
                q.append(i)
                way[i] = way[now] + 1
                if i == end:
                    return way[end]
    return -1


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
else:
    print(BFS())