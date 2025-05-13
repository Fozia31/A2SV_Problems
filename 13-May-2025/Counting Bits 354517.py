# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:

        #  method-1
        # ans = []
        # for i in range(n + 1):
        #     ans.append(bin(i).count("1"))
        # return ans
        
        #  method-2
        # ans = []
        # for i in range(n + 1):
        #     ans.append(i.bit_count())
        # return ans

                #  method-3
        # res = []
        # for num in range(n + 1):
        #     count = 0
        #     for i in range(32):
        #         if num & (1 << i) != 0:
        #             count += 1
        #     res.append(count)
        # return res

        #  method-4
        res = []
        for num in range(n + 1):
            count = 0
            while num >0:
                if num & 1 != 0:
                    count += 1
                num = num >> 1
            res.append(count)
        return res



        