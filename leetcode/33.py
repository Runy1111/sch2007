class Solution:
    def search(self, nums: list[int], target: int) -> int:
        k = 0
        for i in range(1, len(nums)):
            if 