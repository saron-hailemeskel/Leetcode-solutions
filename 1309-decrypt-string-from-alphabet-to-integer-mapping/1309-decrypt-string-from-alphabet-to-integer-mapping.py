class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i + 2])
                ans.append(chr(num + ord('a') - 1))
                i += 3
            else:
                num = int(s[i])
                ans.append(chr(num + ord('a') - 1))
                i += 1

        return "".join(ans)