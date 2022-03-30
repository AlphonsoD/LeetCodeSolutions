class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPtr, rightPtr = 0, len(height)-1
        maxAmount = 0
        while leftPtr < rightPtr:
            y = min(height[leftPtr], height[rightPtr])
            maxAmount =  max(((rightPtr - leftPtr) * y), maxAmount)
            
            ### Original solution: (I overthought it)
            # if leftPtr != len(height)-1 and rightPtr != 0:
            #     if height[leftPtr] < height[rightPtr] and height[leftPtr+1] > height[rightPtr-1]:
            #         leftPtr += 1
            #     elif height[rightPtr] < height[leftPtr] and height[rightPtr-1] > height[leftPtr+1]:
            #         rightPtr -= 1
            #     elif height[leftPtr] < height[rightPtr]:
            #         leftPtr += 1
            #     else:
            #         rightPtr -= 1
            
            # Simpler solution
            if height[leftPtr] < height[rightPtr]:
                leftPtr += 1
            else:
                rightPtr -= 1
            
        return maxAmount
    
    """
    Why always move the lower-height pointer (even if the next value is even lower)?
    
    Imagine this case:
    [3....<10 sticks>....5] => water between 3, 5 = 3*11 = 33.
    
    If we move our current highest height-pointer (in this case, height[j] = 5), we will always
    get a lower result, even if the next number is larger (in this case, 8):
    [3...<10 sticks>....8,5] => Water is 3*10 = 30 which is lower than before.
    [i                  j  ]
    [3...<10 sticks>....2,5] => Again lower in this case as compared to the maximal
    
    In the case of height[i] == height[j], neither pointer should be moved because reducing the
    width would guarantee a smaller area. Say we decide to move the left pointer:
        - Case 1: The next height value is larger. It doesn't matter because the height limit would still be
                  limited by the pointer that we didn't move
        - Case 2: The next height value is smaller. We now have a smaller height limit and smaller width, which
                  of course will provide a smaller area
    """
    
    