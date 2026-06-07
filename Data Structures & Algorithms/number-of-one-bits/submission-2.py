class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            n = n & (n-1)
            weight += 1
        return weight