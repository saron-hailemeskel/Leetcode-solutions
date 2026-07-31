class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n= len(nums)

        for i in range(n):
            min=i
            for j in range(i+1,n):
                if (nums[j]<nums[min]):
                    min=j
            if(min!=i):
                 nums[i],nums[min]=nums[min],nums[i]

        result=[]
        for i, num in enumerate(nums):
            if(num== target):
                result.append(i)
        
        return result
       
  


