class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Step 1: Count frequency of each character
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        # Step 2: Find first character with frequency 1
        for index, char in enumerate(s):
            if count[char] == 1:
                return index

        return -1