def v_dv(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b[:0:-1]


kod = v_dv(int(input()))
k = 0
ch = 0
ans = ''
while k < len(kod):
    if kod[k] == '0':
        ans += 'Е'
        ch += 1
        k += 1
    elif kod[k] == '1':
        if kod[k+1] == '1':
            ans += 'А'
            ch += 1
            k += 2
        else:
            ans += 'Р'
            k += 2
print(ans)
print(ch)

