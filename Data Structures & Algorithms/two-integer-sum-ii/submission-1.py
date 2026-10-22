class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        res = [0]*2
        while i < j:
            Sum = numbers[i] + numbers[j]
            if Sum == target:
                res[0] = i+1
                res[1] = j+1
                break
            elif Sum > target:
                j-=1
            else:
                i+=1
        return res
            
