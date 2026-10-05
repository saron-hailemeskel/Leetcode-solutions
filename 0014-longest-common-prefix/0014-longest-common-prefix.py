class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        result = ""

        # Go through each character position
        for i in range(len(strs[0])):

            # Take the character from the first string
            current = strs[0][i]

            # Check that position in every other string
            for word in strs:

                # If the word is too short OR the character is different
                if i >= len(word) or word[i] != current:
                    return result

            # If every word had the same character
            result += current

        return result