class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m=len(s),len(p)
        if n<m:
            return[]

        c1,c2=[0]*26,[0]*26
        for i in range(m):
            c1[ord(p[i])-97]+=1
            c2[ord(s[i])-97]+=1

        res=[]
        if c1==c2:
            res.append(0)

        for i in range(m,n):
            c2[ord(s[i])-97]+=1
            c2[ord(s[i-m])-97]-=1
            if c1==c2:
                res.append(i-m+1)

        return res
        