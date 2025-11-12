# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r=0,0
        nums1[:]=nums1[:m]
        while r<len(nums2):
            if l<len(nums1) and nums1[l]< nums2[r]:
                l=l+1
            else:
                nums1.insert(l,nums2[r])
                r=r+1
                l=l+1
        
        return nums1
        
    
