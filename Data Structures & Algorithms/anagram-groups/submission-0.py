class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            sortstring = "".join(sorted(string))
            if sortstring not in seen:
                seen[sortstring] = [string]
            else:
                seen[sortstring].append(string)
        return [value for value in seen.values()]
            

