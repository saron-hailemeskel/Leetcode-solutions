class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum= sum(arr[:k])
        avg=curr_sum/k
        count=0
        if avg >= threshold:
                count+=1

        for i in range(1, len(arr)-k+1):
            curr_sum-= arr[i-1]
            curr_sum+= arr[i+k-1]
            avg=curr_sum/k
            if avg >= threshold:
                count+=1
        return count  
