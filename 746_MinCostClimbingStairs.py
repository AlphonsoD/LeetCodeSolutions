class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = p2 = 0
        for i in range(len(cost)):
            currCost = cost[i] + min(p1, p2)
            p2, p1 = p1, currCost
        return min(p1, p2)
        