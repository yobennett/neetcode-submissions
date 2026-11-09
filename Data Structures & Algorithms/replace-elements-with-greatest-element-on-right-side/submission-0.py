class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        result = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            result[i] = rightMax
            rightMax = max(rightMax, arr[i])
        return result