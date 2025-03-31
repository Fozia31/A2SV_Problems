# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n=len(citations)
        count=0
        for i in range(n):
            if citations[i]>=n-i:
                count=n-i
                break
        return count