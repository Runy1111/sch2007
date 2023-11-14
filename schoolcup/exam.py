num, sum_n = map(int, input().split())
if num * 3 <= sum_n:
    print(0)
else:
    print(- sum_n + num * 3)
