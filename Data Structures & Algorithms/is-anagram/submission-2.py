class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)

        for letter in t:
            if letter not in s_dict or s_dict[letter] == 0:
                return False

            else:
                s_dict[letter] -= 1

        # for key,val in s_dict.items():
        #     if val != 0:
        #         return False

        return True
        