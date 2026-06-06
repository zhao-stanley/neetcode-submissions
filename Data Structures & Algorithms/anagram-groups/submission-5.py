class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        unicode_offset = 97

        for st in strs:
            bits = 26 * [0]
            for char in st:
                bit = ord(char) - unicode_offset
                bits[bit] += 1
            if str(bits) not in seen:
                seen[str(bits)] = [st]
            else:
                seen[str(bits)].append(st)

        return [value for value in seen.values()]




