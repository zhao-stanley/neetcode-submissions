class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        # first, build set for membership check
        elems = set(nums)

        # identify roots (no prior elem)
        roots = set([elem for elem in elems if elem - 1 not in elems])

        # go thru each root
        for root in roots:
            current_len = 1
            base = root
            # keep incrementing until consecutive elem doesn't exist
            while base + 1 in elems:
                base += 1
                current_len += 1
            max_len = max(max_len, current_len)
        return max_len