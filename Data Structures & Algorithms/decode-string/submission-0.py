class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            elif s[i] == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif s[i] == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += s[i]
            i += 1
        return curr_str

            
            