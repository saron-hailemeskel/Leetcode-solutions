class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        result = ""

        for i in range (len(strs[0])):

            current= strs[0][i]

            for word in strs:

                if i >= len(word) or word[i] != current:
                    return result
              
            result+= current

        return result


