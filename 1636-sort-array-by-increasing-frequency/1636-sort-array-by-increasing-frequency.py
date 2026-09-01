class Solution:
    def frequencySort(self, nums):
        # Step 1: Count frequencies
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Merge sort
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        # Step 3: Merge according to the problem rules
        def merge(left, right):
            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):

                # Lower frequency comes first
                if freq[left[i]] < freq[right[j]]:
                    result.append(left[i])
                    i += 1

                # Same frequency -> larger number comes first
                elif freq[left[i]] > freq[right[j]]:
                    result.append(right[j])
                    j += 1

                elif left[i] > right[j]:
                    result.append(left[i])
                    i += 1

                else:
                    result.append(right[j])
                    j += 1

            # Add remaining elements
            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        return merge_sort(nums)