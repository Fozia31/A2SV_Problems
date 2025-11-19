# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(i, prev, cur):
            if i == n:
                res.append(cur)
                return
            if prev != '0':
                dfs(i+1, '0', cur+'0')
            dfs(i+1, '1', cur+'1')
        dfs(0, '', '')
        return res
''