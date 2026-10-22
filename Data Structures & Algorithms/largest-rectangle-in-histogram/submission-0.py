class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                tp = stack.pop()

                width = i if not stack else i - stack[-1] - 1 

                area = max(area, heights[tp]*width)
            stack.append(i)
        while stack:
            tp = stack.pop()

            width = n if not stack else n - stack[-1]-1
            area = max(area, heights[tp]*width)
        return area