class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1, numRows):
            row, prev = [], pascal[i-1]
            left, right = 0, 1
            while right < len(prev):
                row.append(prev[left]+prev[right])
                left, right = left+1, right+1
            row = [1] + row + [1]
            pascal.append(row)
        return pascal