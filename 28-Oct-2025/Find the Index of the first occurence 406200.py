# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)]==needle:
                    return i
                    break
            return -1

        