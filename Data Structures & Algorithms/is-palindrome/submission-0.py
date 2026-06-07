class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        clean = "".join(char for char in lower if char.isalnum())
        reverseclean = clean[::-1]
        return clean == reverseclean

