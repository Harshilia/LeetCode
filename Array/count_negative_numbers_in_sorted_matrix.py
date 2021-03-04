class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        count = 0
        j=0
        i = len(grid) - 1

        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                count+= len(grid[0]) - j
                i-=1
            else:
                j+=1

        return count
