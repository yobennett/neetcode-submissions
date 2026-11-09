class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # frequency counts per character
        counts = {}

        result = 0

        L = 0

        for R in range(len(s)):
            char = s[R]
            counts[char] = counts.get(char, 0) + 1
            while (R - L + 1) - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1
            result = max(result, R - L + 1)
        return result