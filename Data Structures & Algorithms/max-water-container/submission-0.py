class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        result = 0

        while L < R:
            area = (R - L) * min(heights[L], heights[R])
            result = max(result, area)

            # height L <= height R
            # shrink window from L, advance L
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        
        return result