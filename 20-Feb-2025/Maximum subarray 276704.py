# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = prefix_sum = nums[0]
        
        left = 0
        right = 1
        while left <= right:
            if right != len(nums):

                prefix_sum += nums[right]
                max_ = max( max_ , prefix_sum)
                right += 1
                print(max_)

            elif right == len(nums):
                max_ = max(max_ , prefix_sum - nums[left])
                left += 1
        return max_
            
    