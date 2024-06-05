class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time = 0
        last_metal = last_paper = last_glass = -1
    
        for i, g in enumerate(garbage):
            total_time += len(g)
            if 'M' in g:
                last_metal = i
            if 'P' in g:
                last_paper = i
            if 'G' in g:
                last_glass = i

        for i in range(1, len(garbage)):
            if i <= last_metal:
                total_time += travel[i - 1]
            if i <= last_paper:
                total_time += travel[i - 1]
            if i <= last_glass:
                total_time += travel[i - 1]

        return total_time