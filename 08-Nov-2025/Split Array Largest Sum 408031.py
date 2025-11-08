# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution(object):
    def splitArray(self, nums, k):
        def can_split(max_sum):
            count = 1
            curr = 0
            for x in nums:
                if curr + x > max_sum:
                    count += 1
                    curr = x
                    if count > k:
                        return False
                else:
                    curr += x
            return True

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left
