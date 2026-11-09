class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, answer = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                answer = max(answer, count)
            else:
                count = 0
        return answer