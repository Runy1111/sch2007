size, times = map(int, input().split())
mas = input()
pref = [0] * (size + 1)
for i in range(1, size + 1):
    pref[i] = pref[i-1] + ord(mas[i-1]) - 96
for i in range(times):
    l, r = map(int, input().split())
    print(pref[r] - pref[l-1])
