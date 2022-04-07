class Solution:
    
    fibNums = {0:0, 1:1}
    
    def fib(self, n: int) -> int:
        if n in self.fibNums.keys():
            return self.fibNums[n]
        else: 
            self.fibNums[n] = self.fib(n-1) + self.fib(n-2)
            return self.fibNums[n]