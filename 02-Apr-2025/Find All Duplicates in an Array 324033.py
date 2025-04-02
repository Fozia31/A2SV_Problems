# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        counter = Counter(nums)
        ans = []

        for key , value in counter.items():
            if value == 2:
                ans.append(key)

        return ans 
       
    