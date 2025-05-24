# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ans = []
        for num in nums:
            ans.append(int(num))
            
        ans.sort(reverse = True)
        return str(ans[k-1])