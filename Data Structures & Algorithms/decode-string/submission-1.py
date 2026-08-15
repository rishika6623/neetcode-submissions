class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        total = 0
        total_char = ""
        stack = []
        while i < len(s):
            if s[i].isdigit():
                total *= 10
                total += int(s[i])

            elif s[i].isalpha():
                total_char += s[i]

            elif s[i] == "[":
                stack.append(total)
                stack.append(total_char)
                total = 0
                total_char = ""

            elif s[i] == "]":
                prev_str = stack.pop()
                factor = stack.pop()

                total_char = prev_str + factor * total_char

            i += 1

        return total_char