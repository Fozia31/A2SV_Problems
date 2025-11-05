# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution(object):
    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        def findAllOccurrences(s, pattern):
            indices = []
            n, m = len(s), len(pattern)
            for i in range(n - m + 1):
                if s[i:i+m] == pattern:
                    indices.append(i)
            return indices
        
        indicesA = findAllOccurrences(s, a)
        indicesB = findAllOccurrences(s, b)
        
        result = []
        for i in indicesA:
            for j in indicesB:
                if abs(j - i) <= k:
                    result.append(i)
                    break
        
        return result
