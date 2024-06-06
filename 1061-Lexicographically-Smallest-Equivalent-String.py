class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        result=[]
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            while x != parent[x]:
                x = parent[x]
            return x
        def union(a,b):
            ra = find(a)
            rb = find(b)
            parent[ra] = parent[rb] = min(ra,rb)
        for c1,c2 in zip(s1,s2):
            union(c1,c2)            
        for c in baseStr:
            result.append(parent[find(c)])
        return ''.join(result)    