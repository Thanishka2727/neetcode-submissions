class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        j = len(nums) - 1
        carry = 0 
        while j >= 0:
            if nums[j] < 9:
                nums[j] += 1
                return nums

            nums[j] = 0
                
            j-=1
        nums = [1] + nums
        return nums