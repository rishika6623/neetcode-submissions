class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i]))+"."+strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        strings = []
        length = 0
        while i < len(s):
            while s[i] != ".":
                length = length * 10 + int(s[i])
                i+=1
            strings.append(s[i+1 : i + 1 + length])
            i = i + 1 + length
            length = 0

        return strings