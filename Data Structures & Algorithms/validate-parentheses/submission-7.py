class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        opening = {"[": "]", "(": ")", "{": "}"}
        stack = []

        for char in s:
            # if opening char, add corresponding closing char to stack
            if char in opening:
                # top of stack = end of array
                stack.append(opening[char])
            else:
                # as soon as we don't see any more opening chars, we expect
                # to see the correct order closing chars
                # if stack is empty, we're missing opening chars
                if not stack:
                    return False
                closing_char = stack.pop()
                if closing_char != char:
                    return False
        # if we exit and we have remaining items in the stack, 
        # we're missing closing chars
        return not stack
