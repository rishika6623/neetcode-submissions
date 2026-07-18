class Solution:
    def isValid(self, s: str) -> bool:
        chars = {"(":")", "{":"}", "[":"]"}
        stack = []
        for p in s:
            if p in chars:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                b = stack.pop()
                if chars[b] != p:
                    return False
        if len(stack) != 0:
            return False
        return True