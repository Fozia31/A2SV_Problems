# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def canPartition(s, target):
            if not s:
                return target == 0
            for i in range(1, len(s) + 1):
                num = int(s[:i])
                if num <= target and canPartition(s[i:], target - num):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if canPartition(str(sq), i):
                total += sq
        return total

        