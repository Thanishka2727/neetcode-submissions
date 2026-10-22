class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fun(x,n):
            if n == 0:
                return 1
            res = fun(x, n//2)
            res*=res
            if n%2 != 0:
                res*=x
            return res
        if n < 0:
            x = 1/x
            n = abs(n)
        return fun(x, n)
        
        