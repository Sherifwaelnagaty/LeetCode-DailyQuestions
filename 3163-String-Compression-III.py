class Solution:
    def compressedString(self, word: str) -> str:
        
        comp = ""
        N = len(word)
        count = 1
        p = 1
        while p < N:
            if word[p-1] != word[p]:
                comp += str(count) + word[p-1]
                count = 0
            if count == 9:
            
                comp += "9"+ word[p-1]
                count = 0
            count += 1
            p+=1    
        comp+= str(count) + word[N-1]
        return comp            
