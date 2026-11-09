class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n + 1):
            ones = 0
            for i in range(32):
                if num & (1 << i):
                    ones += 1
            result.append(ones)
        return result