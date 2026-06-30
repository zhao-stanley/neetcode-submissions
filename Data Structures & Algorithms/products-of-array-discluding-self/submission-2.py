class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        non_zero_prod = 1
        seen_zero = False
        
        for num in nums:
            prod *= num
            if num == 0:
                if seen_zero:
                    return [0] * len(nums)
                else:
                    seen_zero = True
            else:
                non_zero_prod *= num
        
        return [non_zero_prod if num == 0 else int(prod / num) for num in nums]
            