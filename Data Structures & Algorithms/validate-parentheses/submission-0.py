class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack:
                    return False

                if bracket == ")":
                    expected = "("
                elif bracket == "}":
                    expected = "{"
                else:
                    expected = "["

                if stack[-1] != expected:
                    return False

                stack.pop()

        return len(stack) == 0