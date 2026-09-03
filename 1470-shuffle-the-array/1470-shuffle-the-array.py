class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      i=0
      j=n
      new=[]
      while j< len(nums):
        new.append(nums[i])
        new.append(nums[j])
        i+=1
        j+=1
      return new

