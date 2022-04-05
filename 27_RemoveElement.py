class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removeCount, right, left = 0, len(nums)-1, 0
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
                removeCount += 1
            else:
                left += 1
        return len(nums) - removeCount