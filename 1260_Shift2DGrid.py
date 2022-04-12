class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        iterations = k % (len(grid) * len(grid[0]))
        for i in range(iterations):
            shift = grid[-1].pop()
            for row in range(len(grid)):
                grid[row].insert(0, shift)
                if row != len(grid)-1:
                    shift = grid[row].pop()
        return grid