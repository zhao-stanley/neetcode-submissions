class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area, l, r = 0, 0, len(heights) - 1

        # keep ptrs as far apart as possible to maximize width
        while l < r:
            lb, rb = heights[l], heights[r]
            calc_area = (r-l) * min(lb, rb)
            area = max(calc_area, area)

            # move smaller height ptr -> guarantees area is at maximal width possible
            if lb > rb:
                r -= 1
            else:
                l += 1
        return area


        

