class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()
        sorted_tiles = "".join(sorted(tiles))
        return self.generate_sequences(sorted_tiles, "", 0, seen) - 1

    def factorial(self, n):
        if n <= 1:
            return 1
        res = 1
        for num in range(2, n+1):
            res *= num
        return res
    
    def count_permutations(self, seq):
        tot = self.factorial(len(seq))
        for c in Counter(seq).values():
            tot //= self.factorial(c)
        return tot
    
    def generate_sequences(self, tiles, current, pos, seen):
        if pos >= len(tiles):
            if current not in seen:
                seen.add(current)
                return self.count_permutations(current)
            return 0
        return self.generate_sequences(tiles, current, pos+1, seen) + self.generate_sequences(tiles, current + tiles[pos], pos+1, seen)