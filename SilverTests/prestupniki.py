n = int(input())
m = int(input())
strashni = [0] * n
siklo = [0] * n
for i in range(m):
    kto, kovo = map(int, input().split())
    siklo[kto-1] += 1
    strashni[kovo-1] += 1
ans = -1
for i in range(n):
    if strashni[i] == n-1 and siklo[i] == 0:
        ans = i + 1
        break
print(ans)
