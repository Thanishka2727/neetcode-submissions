class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(idx, nums, res, subset):
            if idx >= len(nums):
                res.append(subset[:])
                return 
            subset.append(nums[idx])
            backtrack(idx+1, nums, res, subset)
            subset.pop()
            backtrack(idx+1, nums, res, subset)
        backtrack(0, nums, res, [])
        return res