class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j] < 0:
                    count += 1
        return count
                
