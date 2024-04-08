mas = input()
ans = 0
if mas[0] == '1':
    ans_now = 0
else:
    ans_now = 1
for i in mas[1:]:
    if i == '1':
        ans_now += 1
ans = ans_now
for i in mas[1:-1]:
    if i == '0':
        ans_now += 1
        ans = max(ans, ans_now)
    else:
        ans_now -= 1
print(ans)
