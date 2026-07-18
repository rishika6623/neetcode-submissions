class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start < end:
            while start<end and not ((s[start] >="a" and s[start] <="z") or (s[start] >="A" and s[start] <= "Z") or (s[start] >="0" and s[start] <= "9")):
                start += 1
            while start<end and not ((s[end] >="a" and s[end] <="z") or (s[end] >= "A" and s[end] <="Z") or (s[end] >="0" and s[end] <="9")):
                end -= 1    
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True