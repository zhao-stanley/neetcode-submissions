class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # if left is sorted half
            if nums[l] <= nums[mid]:
                # target is in left half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                # target is in unsorted half
                else:
                    l = mid + 1
            # if right is sorted half
            else: 
                # target is in unsorted half
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                # target is in left half
                else:
                    r = mid - 1
        return -1
