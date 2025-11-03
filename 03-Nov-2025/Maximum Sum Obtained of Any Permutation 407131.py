# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        diff = [0] * (n + 1)
        for l , r in requests:
            diff[l] += 1
            
            if r + 1 < n:
                diff[r + 1] -= 1
        for i in range(1, n):
            diff[i] += diff[i - 1]

        diff.pop()
        diff.sort()
        nums.sort()

        ans = 0
        for i in range(len(nums)):
            ans = (ans + diff[i] * nums[i])%MOD
        
        return ans