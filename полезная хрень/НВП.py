def binp(nums, find):
    l = -1
    r = len(nums)
    while r - l > 1:
        m = (r + l) // 2
        if nums[m] >= find:
            r = m
        else:
            l = m
    return r


def nvp(nums):
    inf = max(nums) + 1
    dp = [min(nums)-1] + [inf] * len(nums)
    for i in nums:
        q = binp(dp, i)
        dp[q] = i
    i = len(nums)
    while dp[i] == inf:
        i -= 1
    return i


print(nvp([1, 6, 3, 12, 2, 4, 5]))
