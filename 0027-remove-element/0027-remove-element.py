class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        for i in nums:
            if i != val:
                nums[a] = i
                a += 1
        return a
            
            
            
