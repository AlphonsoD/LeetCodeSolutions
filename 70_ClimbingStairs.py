class Solution:
    def climbStairs(self, n: int) -> int:
        vals = {}
        vals[1] = 1
        vals[2] = 2
        for i in range(3, n+1):
            vals[i] = vals[i-1] + vals[i-2]
        return vals[n]
    
"""
How to identify a dynamic programming problem:

    - Can the problem be broken down into smaller subproblems, and can we store the solutions
      to those subproblems to solve bigger subproblems?
    - Problems that involve minimizing/maximizing or counting the number of ways something
      can be done usually require dynamic programming.

Explanation of the solution:

    We can rephrase the problem as "How many ways can we add 1 and 2 to get a number n?".
    Let's say that n=3. Well, we can figure out the solutions for the smaller subproblems first.

    If n=1, then there's only 1 way to get that number, which is just 1 by itself.
    If n=2, then we can either do 1 + 1, or 2.

    To get n=3, we could either add 1 to every solution for n=2:
        (1 + 1) + 1
        (2) + 1
    Or we could add 2 to every solution for n=1:
        (1) + 2
    
    So we could say that f(3) = f(1) + f(2), or in other words, f(3) = f(3-1) + f(3-2).
    In general, we can see that f(n) = f(n-1) + f(n-2).
    
Improvements:
    - Currently, we have O(n) space complexity since we're storing values for every number
      between 1 and n. But looking at the general solution, we can see that we only really
      need to remember the last 2 values f(n-1) and f(n-2), so with each iteration we can
      replace these values with newly calculated ones, giving us a space complexity of O(1).
      (To see what I mean, see https://takeuforward.org/data-structure/dynamic-programming-climbing-stairs/)
"""