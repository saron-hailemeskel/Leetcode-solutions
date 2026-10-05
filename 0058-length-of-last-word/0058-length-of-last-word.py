class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words=s.split()
        last= len(words)-1
        for word in words:
            return len(words[last])