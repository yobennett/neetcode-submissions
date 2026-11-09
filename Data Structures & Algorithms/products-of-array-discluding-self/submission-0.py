class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct, postfixProduct, output = [0] * n, [0] * n, [0] * n

        # prefix
        total = 1
        for i in range(n):
            total *= nums[i]
            prefixProduct[i] = total

        # postfix
        total = 1
        for i in range(n - 1, -1, -1):
            total *= nums[i]
            postfixProduct[i] = total

        # output
        for i in range(n):
            L, R = i - 1, i + 1
            leftProduct = prefixProduct[L] if L >= 0 else 1
            rightProduct = postfixProduct[R] if R < n else 1
            output[i] = leftProduct * rightProduct 

        return output