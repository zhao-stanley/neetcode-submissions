class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums):
            jl = nums[i]
            if jl == 0 and i < len(nums) - 1:
                return False
            if jl + i >= len(nums) - 1:
                return True
            subset = nums[i+1:i+1+jl]
            max_jl = (0, 1)
            for offset, num in enumerate(subset):
                resultant = i + offset + 1 + num
                if resultant > max_jl[0]:
                    max_jl = resultant, offset + 1
                    
            i += max_jl[1]
            
        return i >= len(nums)
