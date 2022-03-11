class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runSum = nums[0]
        maxSum = nums[0]
        for num in nums[1:]:
            runSum += num
            # reset the running sum if the current number is larger than it
            # (meaning we don't care about the numbers that came before anymore)
            if num > runSum:
                runSum = num
            maxSum = max(maxSum, runSum)
        return maxSum
        