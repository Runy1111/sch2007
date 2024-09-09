n = int(input())
a = input()
ans = 0
num = 0
for i in range(n):
    ans += 2 * (i+1) * int(a[i])
    if a[i] == '1':
        num += 1
print(ans - num**2)
