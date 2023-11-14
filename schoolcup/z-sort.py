size = int(input())
mas = sorted(list(map(int, input().split())))
ans = []
k = 0
for i in range(size):
    ans.append(mas[k])
    mas.remove(mas[k])
    if k == 0:
        k = -1
    else:
        k = 0

print(*ans)
