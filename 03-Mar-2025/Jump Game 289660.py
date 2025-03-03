# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # l = 0 
        # while l <len(nums):
        #     if nums[l + 1] - nums[l] >= nums[l + 1]:
        #         return False
                
        #     l += 1


        # return True
        max_  = 0
        for i in range(len(nums)):
            if i > max_:
                return False
                
            max_ = max(max_ , i + nums[i])

        return True


        