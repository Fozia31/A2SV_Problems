# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        s = set(nums)
        ans = []
        for n in range(1 , len(nums) + 1):
            if n not in s :
                ans.append(n)

        return ans





