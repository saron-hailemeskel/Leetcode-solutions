class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(heights)
        m=len(names)
        pair={names[i]:heights[i] for i in range(m)}
        
        for i in range(n):
            for j in range(n-1-i):
                if heights[j]<heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
        return names

  #learned lesson:  pair={names[i]:heights[i] for i in range(m)} converting arrays to dictionaries even if this was not needed
