class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        stack = []

        for letter in s:
            if letter not in match:
                stack.append(letter)
            else:
                if not stack:
                    return False
                if stack.pop() != match[letter]:
                    return False


        if stack:
            return False

        return True