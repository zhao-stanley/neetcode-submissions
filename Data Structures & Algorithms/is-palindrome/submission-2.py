class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            if s[lp].isalnum() and s[rp].isalnum():
                if s[lp].lower() == s[rp].lower():
                    lp += 1
                    rp -= 1
                else:
                    return False
            else:
                if not s[lp].isalnum():
                    lp += 1
                if not s[rp].isalnum():
                    rp -= 1
        return True