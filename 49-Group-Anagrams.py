class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagram = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in Anagram:
                Anagram[sortedWord].append(word)
            else:
                Anagram[sortedWord] = [word]
        return list(Anagram.values())

        