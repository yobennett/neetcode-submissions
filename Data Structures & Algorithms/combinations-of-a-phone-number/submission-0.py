class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return result

        def backtrack(i, curr):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return
            
            digit = digits[i]
            for char in digitToChar[digit]:
                curr.append(char)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])

        return result