class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0 

        right = n-1
        water = 0

        while left < right:

            h = min(heights[left],heights[right])
            water = max(h*(right-left) , water)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return water

