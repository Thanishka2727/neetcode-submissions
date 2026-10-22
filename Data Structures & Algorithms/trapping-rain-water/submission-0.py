class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        left = 0
        right = n-1
        l_ht = height[0]
        r_ht = height[n-1]
        water = 0
        while left < right:
            if height[left] <= height[right]:
                left += 1
                l_ht = max(l_ht, height[left])
                water += l_ht - height[left]
            else:
                right -=1
                r_ht = max(r_ht, height[right])
                water += r_ht - height[right]
        return water
        