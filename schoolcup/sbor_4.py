nho = int(input())
a = []
for i in range(nho):
    b, d = map(int, input().split())
    a.append([b, d])
t = int(input())
for i in range(t):
    l, r, k = map(int, input().split())
    mi = 100000000000000000
    for j in range(l-1, r):
        mi = min(mi, a[j][0] + a[j][1] * (k-1))
    print(mi)