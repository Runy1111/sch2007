n, k = map(int, input().split())
nums = list(map(int, input().split()))

inds = {
    0: 6,
    1: 2,
    2: 6,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

grps = {
    2: -1,
    3: -1,
    4: -1,
    5: -1,
    6: -1,
    7: -1,
}

for num in nums:
    grps[inds[num]] = max(grps[inds[num]], num)

ans = []
x = n
min = 5
while x > 0:

