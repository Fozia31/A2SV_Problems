# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            if nums[i] < ans:
                ans = nums[i]
        return ans
            
        