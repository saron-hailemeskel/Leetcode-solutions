class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count= [0]*1001
        for num in arr1:
            count[num]+=1
        result=[]
        for num in arr2:
            freq=count[num]
            result.extend([num]*freq)
            count[num]=0
        for num in range(1001):
           freq = count[num]
           result.extend([num] * freq)
              
        return result


        
        