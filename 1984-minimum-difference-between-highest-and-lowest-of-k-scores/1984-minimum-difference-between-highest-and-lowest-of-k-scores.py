class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = k - 1
        minimum = float("inf")

        while r < len(nums):
            minimum = min(minimum, nums[r] - nums[l])
            l += 1
            r += 1

        return minimum