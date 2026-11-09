class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # bitshift it to the right by i
            # logical and with 1 to determine bit (0 or 1)
            bit = (n >> i) & 1
            # append to result by bitshifting to the left (opposite direction)
            result += (bit << (31 - i))
        return result