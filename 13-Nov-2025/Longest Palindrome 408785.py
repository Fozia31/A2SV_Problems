# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution(object):
    def longestPalindrome(self, s):
        counts = Counter(s)
        ans = 0
        has_odd = False
        for count in counts.values():
            ans += (count // 2) * 2    
            if count % 2 == 1:
                has_odd = True
        if has_odd:
            ans += 1
        return ans
