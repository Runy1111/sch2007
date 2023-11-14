def lev(f_str, s_str):
    cash = []
    f_len, s_len = len(f_str), len(s_str)
    for i in range(f_len + 1):
        cash.append([0] * (s_len + 1))
    for i in range(f_len + 1):
        for j in range(s_len + 1):
            if i == 0 and j == 0:
                cash[i][j] = 0
            elif i == 0:
                cash[i][j] = cash[i][j - 1] + 1
            elif j == 0:
                cash[i][j] = cash[i - 1][j] + 1
            else:
                if s_str[j-1] != f_str[i-1]:
                    cash[i][j] = min(cash[i][j - 1], cash[i - 1][j], cash[i - 1][j - 1]) + 1
                else:
                    cash[i][j] = min(cash[i - 1][j] + 1, cash[i][j - 1] + 1, cash[i - 1][j - 1])
    return cash[-1][-1]


print(lev(input(), input()))
