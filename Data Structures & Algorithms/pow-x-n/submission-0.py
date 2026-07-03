class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        for i in range(1, abs(n)+1):
            ans = ans * x if n > 0 else ans / x
        return ans