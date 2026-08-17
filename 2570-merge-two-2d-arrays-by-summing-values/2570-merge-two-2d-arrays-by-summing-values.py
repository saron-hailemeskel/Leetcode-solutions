class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        d = {}
        for id, value in nums1:
            d[id] = value
        for id, value in nums2:
            if id in d:
                d[id] = d[id] + value
            else:
                d[id] = value
        result = []
        for id, value in d.items():
            result.append([id, value])

        
        result.sort()

        return result

              