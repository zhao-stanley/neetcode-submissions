class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(i: int):
            # base cases
            if i == 0 or i == 1:
                return i
            # some int n is the same as n >> 1 + lsb(n) (0 or 1)
            return helper(i >> 1) + helper(i & 1)

        # calculate for each integer from [0,n]
        return [helper(i) for i in range(n+1)]    