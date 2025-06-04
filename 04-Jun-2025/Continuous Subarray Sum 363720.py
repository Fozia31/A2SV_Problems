# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_idx = {0: -1}
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            if k != 0:
                running_sum %= k
            if running_sum in remainder_idx:
                if i - remainder_idx[running_sum] > 1:
                    return True
            else:
                remainder_idx[running_sum] = i
        return False