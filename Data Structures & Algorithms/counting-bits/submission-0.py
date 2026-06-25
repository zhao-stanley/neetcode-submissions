class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = []
        
        def helper(i: int):
            if i == 0 or i == 1:
                return i
            return helper(i >> 1) + helper(i & 1)

        return [helper(i) for i in range(n+1)]    