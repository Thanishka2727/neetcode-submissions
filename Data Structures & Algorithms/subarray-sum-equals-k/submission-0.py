class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp = {0:1}

        pref = 0 
        cnt = 0

        for i in range(len(nums)):

            pref += nums[i]

            cnt += mpp.get(pref-k,0)

            mpp[pref] = mpp.get(pref,0)+1
        return cnt
        