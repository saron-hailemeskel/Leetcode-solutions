class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[nums[i]**2 for i in range (len(nums))]
        l=0
        r=len(nums)-1
        result=[]
        while (l<=r):
            if nums[l]< nums[r]:
                result.append(nums[r])
                r-=1
            else:
                result.append(nums[l])
                l+=1
         
        return result[::-1]




        