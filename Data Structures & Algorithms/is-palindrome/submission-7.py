class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < len(s) -1 and not s[left].isalpha() and not s[left].isdigit():
                left += 1

            while right > 0 and not s[right].isalpha() and not s[right].isdigit():
                right -= 1

            if left<right:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1

        return True