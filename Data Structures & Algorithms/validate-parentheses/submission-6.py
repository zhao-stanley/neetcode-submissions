class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        opening = {"[": "]", "(": ")", "{": "}"}
        stack = []

        for char in s:
            if char in opening:
                stack.append(opening[char])
            else:
                if not stack:
                    return False
                closing_char = stack.pop()
                if closing_char != char:
                    return False

        return not stack
