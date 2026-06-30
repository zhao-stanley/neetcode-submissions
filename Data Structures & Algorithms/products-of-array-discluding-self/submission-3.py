class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, non_zero_prod = 1, 1
        multiple_zeroes = False
        
        for num in nums:
            prod *= num
            if num == 0:
                if multiple_zeroes:
                    return [0] * len(nums)
                else:
                    multiple_zeroes = True
            else:
                non_zero_prod *= num
        
        return [non_zero_prod if num == 0 else int(prod / num) for num in nums]
            