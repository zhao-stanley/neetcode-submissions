class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -1001
        currentsum = 0

        for num in nums:
            currentsum += num
            maxsum = max(currentsum, maxsum)
        
            if currentsum < 0:
                currentsum = 0
        return maxsum