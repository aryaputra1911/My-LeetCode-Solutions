class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = [Counter(nums)]
        for counter in counter:
            for i,j in counter.items():
                if j == 1:
                    return i
        
        