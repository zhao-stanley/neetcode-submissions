class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        sl = s.lower()

        while lp < rp:
            if sl[lp].isalnum() and sl[rp].isalnum():
                if sl[lp] == sl[rp]:
                    lp += 1
                    rp -= 1
                else:
                    return False
            else:
                if not sl[lp].isalnum():
                    lp += 1
                if not sl[rp].isalnum():
                    rp -= 1
        return True