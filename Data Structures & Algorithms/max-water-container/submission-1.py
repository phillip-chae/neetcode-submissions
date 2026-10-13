class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1

        def area(l, r):
            h = min(heights[l], heights[r])
            w = r - l
            return h * w
        
        a = 0
        while l < r:
            if (c_a := area(l, r)) > a:
                a = c_a
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return a