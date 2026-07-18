class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique_grams = 0
        return_string = []
        seen_string = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            # print(sorted_string)
            # print(seen_string)
            # print(return_string)
            if sorted_string in seen_string:
                return_string[seen_string[sorted_string]].append(string)
            else:
                seen_string[sorted_string] = unique_grams
                return_string.append([string])
                unique_grams+=1
        return return_string