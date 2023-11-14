x = int(input())
ans = 0
i = 5
while x != 0:
    ans += x // i
    x %= i
    i -= 1
print(ans)
