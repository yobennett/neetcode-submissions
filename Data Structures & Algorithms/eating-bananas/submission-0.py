class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        result = right

        while left <= right:

            mid = (left + right) // 2
            k = mid

            total = 0
            for p in piles:
                total += math.ceil(p / k)
            if total <= h:
                result = k
                right = mid - 1
            else:
                left = mid + 1
        
        return result