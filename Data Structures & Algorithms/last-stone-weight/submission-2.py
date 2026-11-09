import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            stone1 = abs(heapq.heappop(stones))
            stone2 = abs(heapq.heappop(stones))

            diff = abs(stone2 - stone1)
            if diff > 0:
                heapq.heappush(stones, -1 * diff)

        # no stones left
        if len(stones) == 0:
            return 0
        
        # one stone left
        return abs(stones[0])