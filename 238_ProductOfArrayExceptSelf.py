class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # first pass - prefixes
        prefix, postfix = nums[0], nums[-1]
        for i in range(1, len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums)-2, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res