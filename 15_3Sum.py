class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for anchor in range(len(nums) - 2):
            if anchor > 0 and nums[anchor] == nums[anchor-1]:
                continue
            left, right = anchor + 1, len(nums)-1
            while left < right:
                threeSum = nums[anchor] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([nums[anchor], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return result