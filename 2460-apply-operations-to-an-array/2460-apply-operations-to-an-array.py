class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[j]:
                nums[i] *= 2
                nums[j] = 0
            j += 1
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1

        return nums