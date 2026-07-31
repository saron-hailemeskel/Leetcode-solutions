class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i,word in enumerate(words):
            for j in word:
                if j==x:
                    result.append(i)
                    break
        return result