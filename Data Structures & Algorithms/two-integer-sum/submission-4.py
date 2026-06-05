class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {target-num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if num in complements and i != complements[num]:
                return [i, complements[num]]
    
