cap_num = int(input())
cap = sorted(list(map(int, input().split())))
cap_s = 0
tsh_num = int(input())
tsh = sorted(list(map(int, input().split())))
tsh_s = 0
pan_num = int(input())
pan = sorted(list(map(int, input().split())))
pan_s = 0
bot_num = int(input())
bot = sorted(list(map(int, input().split())))
bot_s = 0
ans = [cap[cap_s], tsh[tsh_s], pan[pan_s], bot[bot_s]]
sti_max = max(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s]) - min(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s])

while 1 == 1:
    if min(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s]) == cap[cap_s]:
        if cap_s != cap_num - 1:
            cap_s += 1
        else:
            break

    elif min(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s]) == tsh[tsh_s]:
        if tsh_s != tsh_num - 1:
            tsh_s += 1
        else:
            break

    elif min(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s]) == bot[bot_s]:
        if bot_s != bot_num - 1:
            bot_s += 1
        else:
            break

    else:
        if pan_s != pan_num - 1:
            pan_s += 1
        else:
            break

    if max(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s]) - min(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s]) < sti_max:
        sti_max = max(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s]) - min(cap[cap_s], tsh[tsh_s], bot[bot_s], pan[pan_s])
        ans = [cap[cap_s], tsh[tsh_s], pan[pan_s], bot[bot_s]]


print(*ans)
