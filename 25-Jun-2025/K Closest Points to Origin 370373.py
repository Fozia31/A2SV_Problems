# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            dist = x * x + y * y
            distances.append((dist, [x, y]))
        distances.sort()
        result = []
        for i in range(k):
            result.append(distances[i][1])
        return result