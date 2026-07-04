class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = list(set(nums))
        b = nums
        if sorted(a) == sorted(b):
            return False
        if sorted(a) != sorted(b):
            return True