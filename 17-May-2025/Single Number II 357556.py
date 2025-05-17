# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = set(nums)

        for n in num:
            if nums.count(n) == 1:
                return n