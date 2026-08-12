class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxx = float("-inf")
        curr_sum = sum(nums[:k])
        maxx= curr_sum

        for i in range(1, len(nums)-k+1):
            curr_sum -= nums[i-1]
            curr_sum += nums[k+i-1]
            maxx= max(curr_sum,maxx)
        return maxx/ k
        