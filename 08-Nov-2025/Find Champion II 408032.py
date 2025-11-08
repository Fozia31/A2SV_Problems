# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        in_deg = [0] * n
        for u, v in edges:
            in_deg[v] += 1
        ans = -1
        count0 = 0
        for i in range(n):
            if in_deg[i] == 0:
                ans = i
                count0 += 1
        return ans if count0 == 1 else -1
