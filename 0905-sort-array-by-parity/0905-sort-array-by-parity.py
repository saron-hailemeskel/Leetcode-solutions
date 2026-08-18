class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j=0
        for i in range(1,len(nums)):
            if nums[j]%2==0:
                j+=1
                continue
            if nums[i]%2==0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums


        