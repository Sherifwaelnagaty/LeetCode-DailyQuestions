class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        def dfs(counter):
            total_sequences = 0
            for char in counter:
                if counter[char] > 0:
                    total_sequences += 1
                    counter[char] -= 1
                    total_sequences += dfs(counter)
                    counter[char] += 1
            return total_sequences
        return dfs(count)
