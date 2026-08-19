class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = []
        groups = defaultdict(list)
        for string in strs:
            # groups[string.sort()].append(string)
            groups["".join(sorted(string))].append(string)

        for key, value in groups.items():
            total.append(value)

        return total