class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [nums[0]], [nums[-1]]
        output = []
        
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i])
            suffix.append(suffix[i-1] * nums[len(nums) - 1 - i])
        
        for i in range(len(nums)):
            pk = i - 1
            sk = len(nums) - 1 - i - 1
            if pk >= 0 and sk >= 0:
                output.append(prefix[pk] * suffix[sk])
            elif pk >= 0:
                output.append(prefix[pk])
            else:
                output.append(suffix[sk])
        return output
