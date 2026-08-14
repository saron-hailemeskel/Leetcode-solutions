from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window_count = Counter()

        result = []
        k = len(p)

        for i in range(len(s)):
            # Add the new character
            window_count[s[i]] += 1

            # Keep window size equal to len(p)
            if i >= k:
                window_count[s[i - k]] -= 1

                if window_count[s[i - k]] == 0:
                    del window_count[s[i - k]]

            # Check if current window is an anagram
            if window_count == p_count:
                result.append(i - k + 1)

        return result