class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Sum = sum(nums)
        n = len(nums)
        actualSum = (n * (n+1))//2
        missing = actualSum - Sum
        return missing
        