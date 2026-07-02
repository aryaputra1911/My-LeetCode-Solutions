class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = digits
        a = ""
        for i in nums:
            a += str(i)
        plus = int(a)+1
        return list(map(int, str(plus)))