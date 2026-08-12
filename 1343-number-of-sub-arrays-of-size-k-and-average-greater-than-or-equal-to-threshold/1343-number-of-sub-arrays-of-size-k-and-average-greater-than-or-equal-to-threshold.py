class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum= sum(arr[:k])
        target= k* threshold
        count=0
        if  curr_sum >= target:
                count+=1

        for i in range(1, len(arr)-k+1):
            curr_sum-= arr[i-1]
            curr_sum+= arr[i+k-1]
            
            if  curr_sum >= target:
                count+=1
        return count  
