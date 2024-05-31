class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        p1=0
        while p1<len(s): 
            p2=0
            while p2<len(t):
                if s[p1] == t[p2]:
                    result+= abs(p1-p2)
                p2+=1
            p1+=1    
        return result          
        