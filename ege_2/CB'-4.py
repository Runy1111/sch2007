n = int(input())
for uga in range(n):
    a = int(input())
    ans_1 = 0
    ans_2 = []
    while a != 0:
        ans_1 += 1
        if a % 4 == 1:
            ans_2.append(1)
            a -= 1
        elif a % 4 == 3:
            ans_2.append(-1)
            a += 1
        else:
            ans_2.append(0)
        a //= 2
    print(ans_1)
    print(*ans_2)