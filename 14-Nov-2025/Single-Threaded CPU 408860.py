# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution(object):
    def getOrder(self, tasks):
        import heapq
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        res = []
        h = []
        time = tasks[0][0]
        i = 0
        n = len(tasks)

        while i < n or h:
            while i < n and tasks[i][0] <= time:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1

            if h:
                pt, idx = heapq.heappop(h)
                time += pt
                res.append(idx)
            else:
                time = tasks[i][0]

        return res
