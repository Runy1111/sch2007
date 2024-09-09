n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
k = 1
q = 0
for i in range(m-1, 0, -1):
    b = (a[i] - a[i-1]) * k
    if b <= n:
        n -= b
    else:
        q = 1
        break
