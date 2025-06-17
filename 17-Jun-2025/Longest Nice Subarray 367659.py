# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        mask = 0
        res = 0
        for right in range(len(nums)):
            while mask & nums[right]:
                mask ^= nums[left]
                left += 1
            mask |= nums[right]
            res = max(res, right - left + 1)
        return res