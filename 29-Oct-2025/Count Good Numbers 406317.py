# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_num = (n + 1) // 2
        odd_num = n // 2
        MOD = 10**9 + 7
        result1 = pow( 5 ,even_num , MOD)
        result2 = pow(4 , odd_num , MOD)
        return (result1 * result2) % MOD
        
                               
        