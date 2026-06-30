class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        a = list(map(int, str(x)))
        return a == a[::-1]
        
        