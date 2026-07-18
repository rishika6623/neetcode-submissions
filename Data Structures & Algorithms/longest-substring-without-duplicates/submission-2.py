class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length = 0
        # start = 0
        # seen = {}
        # for i in range(len(s)):
        #     length = max(length, i-start)
        #     if s[i] in seen:
        #         start = seen[s[i]]+1
        #     seen[s[i]] = i
        # return length
        length = 0
        start = 0
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                start = max(start, seen[s[i]]+1)
            
            length = max(length, i-start+1)
            seen[s[i]] = i
        return length