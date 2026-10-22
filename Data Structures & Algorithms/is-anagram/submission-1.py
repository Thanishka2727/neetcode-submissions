from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mpp1 = Counter(s)
        for char in t:
            if char in mpp1:
                mpp1[char]-=1
                if mpp1[char]==0:
                    del mpp1[char]
        if len(mpp1) == 0:
            return True
        else:
            return False