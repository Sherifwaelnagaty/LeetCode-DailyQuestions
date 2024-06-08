class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        lists=[0]*len(words)
        for word in words:
            lists[int(word[-1])-1]=word[:-1]      
        return " ".join(lists)        

