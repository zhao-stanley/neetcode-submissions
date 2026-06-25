class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = {}
        output = []
        def helper(i: int):
            # base cases
            if i == 0 or i == 1:
                if i not in dp:
                    dp[i] = i
                return i
            # some int n is the same as n >> 1 + lsb(n) (0 or 1)
            bits = helper(i >> 1) + helper(i & 1)
            if i not in dp:
                dp[i] = bits
            return bits

        for i in range(n+1):
            if i not in dp:
                dp[i] = helper(i)
            output.append(dp[i])

        # calculate for each integer from [0,n]
        return output 