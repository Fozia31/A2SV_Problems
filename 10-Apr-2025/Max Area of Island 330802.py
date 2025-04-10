# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        def dfs(row , col ):

            nonlocal count
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1 :
                count += 1
                grid[row][col] = 0

                dfs(row + 1, col)
                dfs(row - 1 , col)
                dfs(row , col + 1)
                dfs(row  , col - 1)
                
            else:
                return



            return count
        count = 0
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row , col)
                    res = max(res , count)
                    count = 0 
                    
        return res
         





