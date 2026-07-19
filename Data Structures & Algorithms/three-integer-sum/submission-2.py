class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        # get sorted order -> we only examine values to the right
        nums.sort()

        # iterate every num
        for i, num in enumerate(nums):
            # skip duplicate values
            if i > 0 and num == nums[i-1]:
                continue
            # assume num = smallest index, two ptrs on remaining elems
            # s.t. num + l + r = 0
            remaining = 0 - num
            l = i + 1
            r = len(nums) - 1

            while l < r:
                tot = nums[l] + nums[r]
                if tot == remaining:
                    triplets.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # check if same as prev elem, if so, skip
                    # since we dedup l and r has to sum to remaining, we won't get a dupe triplet
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif tot < remaining:
                    l += 1
                else:
                    r -= 1
        return triplets
        
                
                