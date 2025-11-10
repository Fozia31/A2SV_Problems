# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

from collections import defaultdict
import heapq

class Solution(object):
    def maxRemoval(self, nums, queries):
        n = len(nums)
        q = len(queries)
        diff_all = [0] * (n + 1)
        for l, r in queries:
            diff_all[l] += 1
            if r + 1 <= n:
                diff_all[r + 1] -= 1
        coverage_all = [0] * n
        cur = 0
        for i in range(n):
            cur += diff_all[i]
            coverage_all[i] = cur
            if coverage_all[i] < nums[i]:
                return -1
        queries_with_index = sorted([(l, r, idx) for idx, (l, r) in enumerate(queries)], key=lambda x: x[0])
        heap = []
        j = 0
        diff_selected = [0] * (n + 1)
        curr_selected = 0
        used = [0] * q
        for i in range(n):
            curr_selected += diff_selected[i]
            while j < q and queries_with_index[j][0] <= i:
                lq, rq, idxq = queries_with_index[j]
                heapq.heappush(heap, (-rq, idxq))
                j += 1
            while heap and -heap[0][0] < i:
                heapq.heappop(heap)
            while curr_selected < nums[i]:
                if not heap:
                    return -1
                neg_r, idxq = heapq.heappop(heap)
                r_selected = -neg_r
                l_selected, r_selected_original = queries[idxq]
                if used[idxq]:
                    continue
                used[idxq] = 1
                diff_selected[l_selected] += 1
                if r_selected_original + 1 <= n:
                    diff_selected[r_selected_original + 1] -= 1
                curr_selected += 1
        used_count = sum(used)
        return q - used_count
