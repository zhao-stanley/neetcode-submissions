class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        opening = {"[": "]", "(": ")", "{": "}"}
        stack = []

        for char in s:
            if char in opening:
                stack.insert(0, opening[char])
            else:
                if not stack:
                    return False
                closing_char = stack.pop(0)
                if closing_char != char:
                    return False
        return not stack
