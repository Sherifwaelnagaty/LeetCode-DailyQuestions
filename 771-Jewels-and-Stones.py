class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        p1 = 0
        result = 0
        while p1<len(jewels):
            p2 = 0
            while p2<len(stones):
                if jewels[p1]==stones[p2]:
                    result+=1
                p2+=1
            p1+=1
        return result
