from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        left = 0
        n = len(nums)
        ans = []

        for right in range(n):

            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            q.append(right)

            if right-left+1 > k:
                if q and q[0] == left:
                    q.popleft()
                left += 1
            if right - left + 1 == k:
                if q:
                    ans.append(nums[q[0]])
        return ans


        