n = int(input())
x0, y0 = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
queue = [[y0, x0]]
color = a[y0][x0]
while len(queue) != 0:
    now = queue.pop(0)
    if a[now[0]][now[1]] == color:
        a[now[0]][now[1]] = 2
        if now[0] != 0:
            queue.append([now[0]-1, now[1]])
        if now[0] != n-1:
            queue.append([now[0]+1, now[1]])
        if now[1] != 0:
            queue.append([now[0], now[1]-1])
        if now[1] != n-1:
            queue.append([now[0], now[1]+1])

for i in a:
    print(*i)
