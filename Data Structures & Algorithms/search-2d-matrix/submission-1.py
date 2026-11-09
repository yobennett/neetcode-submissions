class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols, rows = len(matrix[0]), len(matrix)

        # binary search for row
        top, bot = 0, rows - 1
        while top <= bot:
            mid = (top + bot) // 2
            row = matrix[mid]
            if target > row[-1]: # check largest value in row
                top = mid + 1
            elif target < row[0]: # check smallest value in row
                bot = mid - 1
            else:
                break

        # check row in bound
        if not (top <= bot):
            return False

        # binary search for col
        row = matrix[(top + bot) // 2] # recalculate row
        left, right = 0, cols
        while left <= right:
            mid = (left + right) // 2
            if target > row[mid]:
                left = mid + 1
            elif target < row[mid]:
                right = mid - 1
            else:
                return True

        return False