class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the last index of each character
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        result = []
        start = 0
        end = 0

        for i in range(len(s)):
            # Extend the partition to the last occurrence
            # of the current character
            end = max(end, last[s[i]])

            # We can close the partition
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result