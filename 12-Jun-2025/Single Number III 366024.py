# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for num in nums:
            xor ^= num

        diff_bit = xor & -xor

        result = [0, 0]
        for num in nums:
            if num & diff_bit:
                result[0] ^= num
            else:
                result[1] ^= num

        return result     