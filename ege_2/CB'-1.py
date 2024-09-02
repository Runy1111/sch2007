bl, pr, bag = map(int, input().split())
wp = list(map(int, input().split()))
wb = []
w_now = 0
for i in range(bl):
    bl_now = list(map(int, input().split()))
    for j in range(pr):
        w_now += bl_now[j] * wp[j]
    wb.append(w_now)
    w_now = 0
wb.sort()

ans = 0
for i in range(bl):
    if bag - wb[i] < 0:
        break
    bag -= wb[i]
    ans += 1
print(ans)
