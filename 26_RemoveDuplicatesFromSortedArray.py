class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        anchor = 0
        uniqueNumCount = 1
        for i in range(len(nums)):
            if nums[i] != nums[anchor]:
                anchor += 1
                nums[anchor] = nums[i]
                uniqueNumCount += 1
        return uniqueNumCount