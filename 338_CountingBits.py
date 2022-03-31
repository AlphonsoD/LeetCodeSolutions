class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ### Original solution -> O(n log n)
        # result = list(range(n+1))
        # for i in range(n+1):
        #     count = 0
        #     while (result[i] > 0):
        #         count = count + 1 if result[i] % 2 == 1 else count
        #         result[i] = result[i] >> 1
        #     result[i] = count
        # return result
        
        ### Faster solution: 
        # If you divide num by 2, then the number of bits is either
        #   - countBits(num/2) + 1 for odd, or
        #   - countBits(num/2) for even
        # For powers of 2, there is only 1 bit
        # So keep track of all the numbers of bits we've seen so far (memoization)
        result, power = [], 1
        
        for i in range(n+1):
            if i < 2 ** power:
                # odd case
                if i % 2 == 1:
                    val = result[i>>1]
                    result.append(val+1)
                    result[i] = val+1
                # even case
                else:
                    val = result[i>>1] if i != 0 else 0
                    result.append(val)
                    result[i] = val
            else:
                power += 1
                result.append(1) # since it's guaranteed to be a power of 2, which only has 1 bit
                
        return result
    
    