class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #nums.sort()
       # i=0
        #for j in range(1,len(nums)):
         #   if nums[i]== nums[j]:
          #      return True
           # else:
            #    i+=1
        #return False
        hashset=set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False