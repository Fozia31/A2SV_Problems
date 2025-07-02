# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            j = 0
            i = 0
            match = True
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    match = False
                    break
                i += 1
            if j != len(pattern):
                match = False
            res.append(match)
        return res