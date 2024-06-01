class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        p1=0
        ans=[]
        while p1<len(words):
            p2=0
            while p2<len(words[p1]):
                if words[p1][p2] == x:
                    ans.append(p1)
                    break
                p2+=1    
            p1+=1
        return ans        