class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_len = 0
        left, right = 0,0

        while right < len(s):
            if s[right] not in last_seen:
                last_seen[s[right]] = right
                
            else:
                #print(right, left, right - left)
                max_len = max(max_len, right - left)
                target_idx = last_seen[s[right]]
                
                while left <= target_idx:
                    if s[left] in last_seen:
                        del last_seen[s[left]]
                    left += 1
                last_seen[s[right]] = right
                
            right += 1

        return max(max_len, right - left)