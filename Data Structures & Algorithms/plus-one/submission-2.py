class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        j = len(nums) - 1
        carry = 0 
        while j >= 0:
            if nums[j] < 9:
                if carry != 0:
                    nums[j] += carry
                    carry = 0
                else:
                    nums[j] += 1
                break
            else:
                nums[j] = 0
                carry = 1
            j-=1
        if carry != 0:
            nums.insert(0,carry)

        return nums