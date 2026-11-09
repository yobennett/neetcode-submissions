class Solution:
    def romanToInt(self, s: str) -> int:
        symToValue = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        L = 0
        while L < len(s):
            val = symToValue[s[L]]
            if L + 1 < len(s):
                if s[L] == "I" and s[L + 1] in ["V", "X"]:
                    val = symToValue[s[L + 1]] - symToValue[s[L]]
                    L += 1
                elif s[L] == "X" and s[L + 1] in ["L", "C"]:
                    val = symToValue[s[L + 1]] - symToValue[s[L]]
                    L += 1
                elif s[L] == "C" and s[L + 1] in ["D", "M"]:
                    val = symToValue[s[L + 1]] - symToValue[s[L]]
                    L += 1

            total += val
            L += 1

        return total