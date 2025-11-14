# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxOr = 0
        for num in nums:
            maxOr |= num
        
        self.count = 0
        n = len(nums)
        
        def dfs(i, currentOr):
            if i == n:
                if currentOr == maxOr:
                    self.count += 1
                return
            dfs(i + 1, currentOr)
            dfs(i + 1, currentOr | nums[i])
        
        dfs(0, 0)
        return self.count
