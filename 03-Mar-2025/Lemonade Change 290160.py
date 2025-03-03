# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = 0
        count_ten = 0

        for j in bills:

            
            if j == 5:
                count_five += 1

            elif j == 10:
                if count_five > 0:
                    count_five -= 1
                    count_ten += 1
                else:
                    return False

            elif j == 20:
                if count_five > 0 and count_ten > 0 :
                    count_five -= 1
                    count_ten -= 1
                elif count_five > 2:
                    count_five -= 3

                else:
                    return False


        return True



        