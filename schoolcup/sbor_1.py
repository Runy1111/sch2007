n, l = map(int, input().split())
ans = 0
mas = [0]
k = 1
now = 1
for i in range(4*l-3):
    if now == l:
        k = -1
    elif now == 1:
        k = 1
    mas.append(now)
    now += k
mas = mas[1:]

for i in range(n):
    num, t_p, t_o = map(int, input().split())
    if t_o >= l * 2 - 2:
        ans += 1
    else:
        t_p = (t_p - 1) % (2*l-2)
        if num in mas[t_p:t_p+t_o]:
            ans += 1
print(ans)
