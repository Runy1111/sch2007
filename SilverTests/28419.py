f_str = input()
s_str = input()
len_1 = len(f_str)
len_2 = len(s_str)
if '*' in f_str and '*' in s_str:
    print("No solution!")
elif '*' in f_str:
    print(s_str.replace('?', 'A'))
elif '*' in s_str:
    print(f_str.replace('?', 'A'))
else:
    cash = [[0] * (len_1 + 1)]
    for i in range(len_2):
        cash.append([0] * (len_1 + 1))
    prev = []

    for i in range(1, len_2 + 1):
        for j in range(1, len_1 + 1):
            if f_str[j - 1] == s_str[i - 1] or s_str[i - 1] == '?' or f_str[j - 1] == '?':
                cash[i][j] = cash[i - 1][j - 1] + 1
            else:
                cash[i][j] = max(cash[i - 1][j], cash[i][j - 1])

    while cash[i][j] != 0:
        if f_str[j - 1] != s_str[i - 1] and s_str[i - 1] != '?' and f_str[j - 1] != '?':
            if cash[i - 1][j] > cash[i][j - 1]:
                i -= 1
            else:
                j -= 1
        else:
            if f_str[j - 1] == '?':
                if s_str[i - 1] == '?':
                    prev.append('A')
                prev.append(s_str[i - 1])
            else:
                prev.append(f_str[j - 1])
            i -= 1
            j -= 1
    print(''.join(prev[::-1]))

