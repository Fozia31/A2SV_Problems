# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = nums1 + nums2
        n = len(merged_array)
        merged_array.sort()
    
        if n%2 != 0:
            return merged_array[n//2]
        else:
            med = merged_array[n//2] + merged_array[n//2 - 1]
            return med/2.0