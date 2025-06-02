# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict_ = defaultdict( int )
        dict_[0] = 1
        count = prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            rem_ = prefix_sum - goal
            
            count += dict_[rem_]
    
            dict_[prefix_sum] += 1
        return count
        