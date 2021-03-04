class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
#         if not grid:
#             return 0
#         islands = 0
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     self.dfs(grid,i,j)
#                     islands +=1
#         return islands
    
#     def dfs(self, grid, i, j):
#         if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == '0':
#             return
#         grid[i][j] = '0'
#         self.dfs(grid, i+1, j)
#         self.dfs(grid, i-1, j)
#         self.dfs(grid, i, j+1)
#         self.dfs(grid, i, j-1)

        self.grid = grid
        self.stack = []
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.stack.append((i,j))
                    islands += 1
                    self.dfs()
                    
        return islands
    
    def dfs(self):
        while self.stack:
            row, column = self.stack.pop()
            self.grid[row][column] = '0'

            for r,c in self.directions:
                gridR, gridC = row+r, column+c

                if 0<=gridR<len(self.grid) and 0<=gridC<len(self.grid[0]) and self.grid[gridR][gridC] == '1':
                    self.stack.append((gridR,gridC))


    