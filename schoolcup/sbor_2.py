def DFS(reb, isk, a, kol, was, nom):
    was.append(nom)
    if a[nom] == isk[kol]:
        kol += 1
    if kol == len(isk):
        return 1
    ans = 0
    for i in reb[nom]:
        if i not in was:
            ans += DFS(reb, isk, a, kol, was, i)
    if ans != 0:
        return 1
    return 0


q = int(input())
for i in range(q):
    n = int(input())
    a = input()
    a = 'Ы'+a
    reb = dict()
    for j in range(n-1):
        x, y = map(int, input().split())
        if x in reb:
            reb[x].append(y)
        else:
            reb[x] = [y]
        if y in reb:
            reb[y].append(x)
        else:
            reb[y] = [x]
    isk = input()
    st = []
    for j in range(1, n+1):
        if a[j] == isk[0]:
            st.append(j)
    w = 0
    if len(isk) == 1:
        if len(st) == 0:
            print(':(')
        else:
            print(':)')
    elif len(reb) == 0:
        print(':(')
    else:
        for now in st:
            if DFS(reb, isk, a, 1, [], now) == 1:
                w = 1
                break
        if w == 1:
            print(':)')
        else:
            print(':(')
