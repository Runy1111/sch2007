def comb(now, ma, size, bef=[0]):
    if now == size:
        print(*bef[1:])
    else:
        for i in range(bef[now] + 1, ma - (size-now) + 2):
            comb(now + 1, ma, size, bef + [i])


comb(0, int(input()), int(input()))
