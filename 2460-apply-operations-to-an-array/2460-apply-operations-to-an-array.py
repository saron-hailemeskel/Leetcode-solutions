class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        j = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[j]:
                nums[i] *= 2
                nums[j] = 0
            j += 1
        z=0
        for i in range(len(nums)):
            if  nums[i] !=0:
                nums[z], nums[i]= nums[i], nums[z]
                z+=1  
        return nums