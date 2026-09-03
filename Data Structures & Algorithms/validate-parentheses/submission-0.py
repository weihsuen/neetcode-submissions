class Solution:
    def isValid(self, s: str) -> bool:

        opening = {'(', "{", "["}
        closing = {"}":"{", ")":"(", "]":"["}

        stack = []

        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif s[i] in closing:
                if not stack or stack[-1] != closing[s[i]]:
                    return False
                else:
                    stack.pop()

        return len(stack) == 0