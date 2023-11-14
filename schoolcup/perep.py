days, num = map(int, input().split())
costs = list(map(int, input().split()))
cash = dict()
ans = []
for serv in costs:
    if serv not in cash:
        cash[serv] = 1
    else:
        cash[serv] += 1
    if cash[serv] == days:
        ans.append(serv)
print(len(ans))
print(*ans)
