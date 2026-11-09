class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 1

        L, R = 0, 1
        result = 1

        prev = ""

        while R < len(arr):
            currNum, prevNum = arr[R], arr[R-1]
            if prevNum < currNum and prev != "<":
                result = max(result, R - L + 1)
                R += 1
                prev = "<"
            elif prevNum > currNum and prev != ">":
                result = max(result, R - L + 1)
                R += 1
                prev = ">"
            else:
                if prevNum == currNum:
                    R += 1
                    L = R - 1
                else:
                    L = R - 1
                prev = ""

        return result