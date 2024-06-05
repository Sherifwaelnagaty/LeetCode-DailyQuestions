class Solution:
    def sortVowels(self, s: str) -> str:
        vowels="AEIOUaeiou"
        q= deque(sorted(c for c in s if c in vowels))
        print(q)
        return "".join(q.popleft() if c in vowels else c for c in s)