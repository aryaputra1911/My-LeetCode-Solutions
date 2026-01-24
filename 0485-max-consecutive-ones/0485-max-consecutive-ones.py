class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0        
        for i in nums:
            if i == 1:
                current += 1
                if current > max:
                    max = current                
            else:
                current = 0
        return max

        

        