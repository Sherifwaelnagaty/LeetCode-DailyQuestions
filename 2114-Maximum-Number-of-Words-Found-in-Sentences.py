class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_space = 0
        for i in sentences:
            max_space = max(max_space, i.count(" ") + 1)
        return max_space