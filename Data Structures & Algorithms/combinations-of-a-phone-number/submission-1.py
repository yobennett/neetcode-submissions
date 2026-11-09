class Solution:
    # Backtracking
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

        # empty digits, return empty result
        if not digits:
            return result

        def backtrack(i, curr):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return

            # current digit            
            digit = digits[i]

            # iterate through each mapped char from current digit
            for char in digitToChar[digit]:
                # add char
                curr.append(char)
                # explore next digit
                backtrack(i + 1, curr)
                # cleanup char
                curr.pop()

        backtrack(0, [])

        return result