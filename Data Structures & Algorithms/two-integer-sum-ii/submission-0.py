class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        
        while L < R:
            result = numbers[L] + numbers[R]
            
            if result == target:
                return [L + 1, R + 1]
            
            if result > target:
                R -= 1
            else:
                L += 1
        
        return []