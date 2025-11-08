# Problem: Minimum Time to Collect All Apples in a Tree - https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            total = 0
            for nei in graph[node]:
                if not visited[nei]:
                    cost = dfs(nei)
                    if cost > 0 or hasApple[nei]:
                        total += cost + 2
            return total

        return dfs(0)
