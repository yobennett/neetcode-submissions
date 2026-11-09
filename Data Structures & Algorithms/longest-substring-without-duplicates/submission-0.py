class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currLength, maxLength = 0, 0
        L = 0
        seen = {}

        for R in range(len(s)):
            if s[R] in seen:
                L = max(seen[s[R]] + 1, L)

            seen[s[R]] = R
            maxLength = max(maxLength, R - L + 1)

        return maxLength