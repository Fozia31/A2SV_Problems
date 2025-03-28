# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def isValid(mid):
            repair_cars = 0
            for n in ranks:
                repair_cars += (int(sqrt((mid // n))))
            
            return repair_cars >= cars

        low = 1
        high = max(ranks) *(cars*cars)
        while low <= high:
            mid = (low+high) // 2
            print(mid)
            if isValid(mid):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1

        return ans
