class Solution(object):
    def twoSum(self, nums, target):
        seen = {}   # number -> index
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in seen:
               return [seen[diff], i]
            
            seen[num] = i
        # nums.sort()
        # p1 = 0
        # p2 = len(nums) -1
        
        # two_sum= False
        # while(p1<p2):
        #     sum = nums[p1]+nums[p2]
        #     if sum == target:
        #         two_sum= True
        #         break
        #     elif sum < target:
        #         p1+=1
        #     else :
        #         p2-=1
        
        # if (two_sum):
        #     return [p1,p2]
        # else: 
        #     return False

    