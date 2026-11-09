class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in range(len(s)):
            char1 = s[i]

            # close
            if char1 in closeToOpen:

                if len(stack) == 0:
                    return False

                char2 = stack.pop()
                if char2 != closeToOpen[char1]:
                    return False

            # open
            else:
                stack.append(char1)

        if len(stack) > 0:
            return False

        return True