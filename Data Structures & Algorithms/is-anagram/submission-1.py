class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for s_char, t_char in zip(s, t):
            seen[s_char] = seen.get(s_char, 0) + 1
            seen[t_char] = seen.get(t_char,0) - 1
        for k,v in seen.items():
            if v != 0:
                return False
        return True
