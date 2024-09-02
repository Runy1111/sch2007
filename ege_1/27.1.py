N, K = map(int, input().split())
pref = [0] + [0] * N
mas = [100000] * K
su = [0] * (N + 1)
for i in range(1, N):
    k = int(input())
    pref[i] = (pref[i - 1] + k) % K
    su[i] = su[i-1] + k
    if su[i] < mas[pref[i]]:
        mas[pref[i]] = su[i]
    if pref[i] % K == 0:
        ans = i


print(mas[(pref[-2] + int(input())) % K])
print(mas)