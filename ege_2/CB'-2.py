h, l = map(int, input().split())
low_p = [-1000] * l
high_p = [-1] * l
scr1 = []
for i in range(h):
    st = input()
    scr1.append(st)
    for j in range(l):
        if st[j] == 'M':
            low_p[j] = i
        elif st[j] == '#' and high_p[j] == -1:
            high_p[j] = i
fall = - low_p[0] + high_p[0] - 1
for i in range(1, l):
    fall = min(fall, - low_p[i] + high_p[i] - 1)
scr2 = [['.']*l for i in range(h)]
for i in range(h):
    for j in range(l):
        if scr1[i][j] == '#':
            scr2[i][j] = '#'
        elif i >= fall:
            if scr1[i-fall][j] == 'M':
                scr2[i][j] = 'M'
    print(*scr2[i], sep='')
