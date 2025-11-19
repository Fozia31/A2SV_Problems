# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(n+1)]
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = [0] * (n+1)
        
        def dfs(node, c):
            color[node] = c
            for nei in graph[node]:
                if color[nei] == c:
                    return False
                if color[nei] == 0 and not dfs(nei, -c):
                    return False
            return True
        
        for i in range(1, n+1):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True
