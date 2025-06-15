# Problem: Interval List Intersections  - https://leetcode.com/problems/interval-list-intersections/description/

class Solution:
    def intervalIntersection(self, firstList, secondList):
        i, j = 0, 0
        res = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                res.append([start, end])

            if a_end < b_end:
                i += 1
            else:
                j += 1

        return res 