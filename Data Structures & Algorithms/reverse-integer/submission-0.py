class Solution:
    def reverse(self, x: int) -> int:
        t = abs(x)
        res = 0
        while t > 0:
            res = res * 10 + t%10 
            t = t//10
        if x < 0:
            res = -1 * res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
