class Solution(object):
    def removeDuplicates(self, nums):
        z=0
        for i in range(1,len(nums)):
            if nums[z]!= nums[i]:
                nums[z+1]=nums[i]
                z+=1
        return z+1