class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def cnt(num):
            count = 0
            while num > 0:

                if num & 1:
                    count+=1
                num>>=1
            return count
        for i in range(0, n+1):
            res.append(cnt(i))
        return res

