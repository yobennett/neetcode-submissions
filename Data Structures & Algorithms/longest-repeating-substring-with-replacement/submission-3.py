class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # frequency counts per character
        counts = {}

        result = 0

        L = 0

        for R in range(len(s)):
            # increment count for current char at R
            charRight = s[R]
            counts[charRight] = counts.get(charRight, 0) + 1

            # condition check if current window is invalid:
            # substring-length - most-frequent-count > K
            while (R - L + 1) - max(counts.values()) > k:
                charLeft = s[L]
                # decrement count for char at L
                counts[charLeft] -= 1
                # shift L
                L += 1

            # max btw substring-length and current result
            result = max(result, R - L + 1)
        return result