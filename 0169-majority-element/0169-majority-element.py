class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a= None
        count=0
        for i in nums:
            if count == 0:
                a = i
            if i == a:
                count += 1
            else:
                count -= 1
        return a
        