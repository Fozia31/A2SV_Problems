# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        res = total
        
        n = len(beans)
        for i in range(n):
            res = min(res, total - beans[i] * (n - i))
        
        return res