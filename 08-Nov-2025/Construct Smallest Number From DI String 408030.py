# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution(object):
    def smallestNumber(self, pattern):
        n = len(pattern)
        result = []
        stack = []
        
        for i in range(n + 1):
            stack.append(i + 1)
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))
        
        return "".join(result)
