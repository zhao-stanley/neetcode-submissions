class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums):
            jl = nums[i]
            if jl == 0 and i < len(nums) - 1:
                return False
            subset = nums[i+1:i+1+jl]
            # (resultant, offset)
            max_resultant = (0, 1)

            for j, num in enumerate(subset):
                # index is 0-based, so offset = index + 1
                offset = j + 1
                resultant = i + offset + num
                if resultant > max_resultant[0]:
                    max_resultant = resultant, offset
                    
            i += max_resultant[1]
            
        return i >= len(nums)
