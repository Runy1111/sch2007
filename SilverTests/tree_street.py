n, m = map(int, input().split())
trees = list(map(int, input().split()))
was = [0] * (m + 1)
v = []
for i in range(n):
    was[trees[i]] += 1
    if trees[i] not in v:
        v.append(trees[i])
    if len(v) == m:
        r = i
        break

l = 0
ans = [l+1, r+1]
ma = r + 1
while 1 == 1:
    if was[trees[l]] >= 2:
        was[trees[l]] -= 1
        l += 1
        if r - l + 1 < ma:
            ma = r - l + 1
            ans = [l+1, r+1]
    else:
        if r == n - 1:
            break
        else:
            r += 1
            was[trees[r]] += 1
print(*ans)
