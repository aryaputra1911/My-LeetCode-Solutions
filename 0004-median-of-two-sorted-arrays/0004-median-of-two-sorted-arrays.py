class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1 + nums2)
        n = len(a)

        mid = n//2

        if n%2 == 0:
            return (a[mid - 1] + a[mid]) / 2
        else:
            return a[mid]