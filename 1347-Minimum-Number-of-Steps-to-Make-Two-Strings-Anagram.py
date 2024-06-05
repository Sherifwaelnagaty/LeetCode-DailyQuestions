class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        print(count_s)
        count_t = Counter(t)
        print(count_t)
        steps = 0
        
        for char in count_s:
            if char in count_t:
                steps += max(0, count_s[char] - count_t[char])
            else:
                steps += count_s[char]
        
        return steps
            
        