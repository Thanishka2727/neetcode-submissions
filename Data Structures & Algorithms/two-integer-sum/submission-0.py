class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        res = [0]*2
        for i in range(len(nums)):
            if target - nums[i] in freq:
                res[0] = freq[target-nums[i]]
                res[1]= i
                break
            else:
                freq[nums[i]]=i
        return res
