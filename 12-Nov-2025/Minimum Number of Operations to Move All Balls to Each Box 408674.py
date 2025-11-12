# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        leftCost = [0] * n
        rightCost = [0] * n

        ballsOnLeft = 0
        for i in range(1, n):
            if boxes[i-1] == '1':
                ballsOnLeft += 1
            leftCost[i] = leftCost[i-1] + ballsOnLeft

        ballsOnRight = 0
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                ballsOnRight += 1
            rightCost[i] = rightCost[i+1] + ballsOnRight

        answer = [0] * n
        for i in range(n):
            answer[i] = leftCost[i] + rightCost[i]

        return answer
