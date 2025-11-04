# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        x_s = [0]
        for num in nums:
            for i in range(len(x_s)):
                x_s.append(x_s[i]^num)
        return sum(x_s)