class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        for char in t:
            seen[char] = seen.get(char,0) - 1
        for k,v in seen.items():
            if v != 0:
                return False
        return True
