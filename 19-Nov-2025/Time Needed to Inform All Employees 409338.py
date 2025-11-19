# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        from collections import defaultdict, deque
        tree = defaultdict(list)
        for i, m in enumerate(manager):
            tree[m].append(i)
        max_time = 0
        queue = deque([(headID, 0)])
        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            for child in tree[node]:
                queue.append((child, time + informTime[node]))
        return max_time
