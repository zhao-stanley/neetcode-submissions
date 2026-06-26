class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        i = 0

        while i < len(nums):
            jl = nums[i]
            if jl + i >= len(nums) - 1:
                return True
            print("current", jl)
            subset = nums[i+1:i+1+jl]
            max_jl = (0, 1, 0)
            for offset, num in enumerate(subset):
                resultant = i + offset + 1 + num
                if resultant > max_jl[2]:
                    max_jl = num, offset + 1, resultant
                    
            print(max_jl)
            if max_jl[0] == 0 and i + max_jl[1] < len(nums) - 1:
                return False
            i += max_jl[1]
            
        
        return i >= len(nums)
