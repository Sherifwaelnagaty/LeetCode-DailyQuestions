class Solution:
    def partitionString(self, s: str) -> int:

        ct, seen = 0, set()
        for si in s:
            if si in seen:
                ct += 1
                seen = set(si)
            else:
                seen.add(si)
                
        return ct + 1