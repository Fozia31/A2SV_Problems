# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution(object):
    def nthUglyNumber(self, n):
        numbers = [1]
        index2 = index3 = index5 = 0

        for _ in range(1, n):
            next_number = min(numbers[index2]*2, numbers[index3]*3, numbers[index5]*5)
            numbers.append(next_number)
            if next_number == numbers[index2]*2:
                index2 += 1
            if next_number == numbers[index3]*3:
                index3 += 1
            if next_number == numbers[index5]*5:
                index5 += 1

        return numbers[-1]
