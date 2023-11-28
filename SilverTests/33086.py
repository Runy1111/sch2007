def bag(num_gold, w_bag, w_gold):
    f = [0] * (w_bag + 1)
    f[0] = 1
    for i in w_gold:
        for j in range(w_bag, i - 1, -1):
            if f[j-i] == 1:
                f[j] = 1
    k = w_bag
    while f[k] == 0:
        k -= 1
    return k


n, w = map(int, input().split())
mas = list(map(int, input().split()))
print(bag(n, w, mas))
