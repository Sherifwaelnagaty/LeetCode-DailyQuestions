class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set('abcdefghijklmnopqrstuvwxyz')
        for letter in sentence.lower():  
            if letter in alphabets:
                alphabets.remove(letter)
            if not alphabets:  
                return True
        return False 