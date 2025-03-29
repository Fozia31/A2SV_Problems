# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l,r = 0, (m*n)-1
        
        if not matrix or not matrix[0]:
            return False

        while l <= r :
            mid = l + (r-l)//2
            md = matrix [mid // n] [mid % n]
            
            if md == target :
                return True
            elif md < target :
                l = mid + 1
            else:
                r = mid - 1
        return False