class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        previous = [1]
        for row in range(1, rowIndex+1):
            new = ([1]*(row+1))
            for num in range(1, len(new)-1):
                new[num] = previous[num-1] + previous[num]
            previous = new
        return previous
