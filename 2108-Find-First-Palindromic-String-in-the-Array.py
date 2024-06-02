class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if self.isPalindrome(i):
                return i 
        return ""    

    def isPalindrome(self, word: str) -> bool:
        return word == word[::-1]            
        