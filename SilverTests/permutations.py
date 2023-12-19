def perm(now, size, dva, bef=''):
    if now == size:
        print(bef)
    else:
        if dva != 2:
            perm(now + 1, size, dva + 1, bef + '2 ')
        perm(now + 1, size, dva, bef + '4 ')
        perm(now + 1, size, dva, bef + '5 ')


perm(0, int(input()), 0)
