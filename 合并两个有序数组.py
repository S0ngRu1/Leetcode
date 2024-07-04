class Solution:
    def merge(self, nums1, m, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]
        nums1.sort()