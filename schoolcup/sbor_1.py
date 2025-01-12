def cost(h,c, h_now):
    c1 = 0
    c2 = 0
    for i in range(len(h)):
        q, w = c[i], h[i]
        c1 += q * abs(h_now-w)
        c2 += q * abs(h_now+1-w)
    if c2 > c1:
        return [1, c1]
    return [0, c1]


n = int(input())
h = list(map(int, input().split()))
c = list(map(int, input().split()))
l = min(h)
r = max(h)
c_now = 0
while r-l > 1:
    h_now = (r+l)//2
    u = cost(h, c, h_now)
    if u[0] == 1:
        r = h_now
        c_now = u[1]
    else:
        l = h_now
print(r, c_now)
