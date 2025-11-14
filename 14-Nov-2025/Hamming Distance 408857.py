# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num1 = bin(x)[2:]
        num2 = bin(y)[2:]
        count = 0
        if len(num1) < len(num2):
            lenn = len(num2) -len(num1)
            num1 = ("0"*lenn) + num1
        else:
            lenn = len(num1) -len(num2)
            num2 = ("0"*lenn) + num2

        for i in range(len(num1)):
            if num1[i]!= num2[i]:
                count += 1

        return count

        