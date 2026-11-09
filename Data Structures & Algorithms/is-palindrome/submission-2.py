class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        L = 0
        R = len(s) - 1
        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1

            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        
        return True