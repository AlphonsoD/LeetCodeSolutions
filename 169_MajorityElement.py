class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ### O(1) space complexity, linear time:
        count, candidate = 0, nums[0]
        for i in range(len(nums)):
            if nums[i] == candidate:
                count += 1
            elif nums[i] != candidate and count > 0:
                count -= 1
            else:
                count, candidate = 1, nums[i]
        return candidate
        
        ### O(N) space complexity, linear time:
        # count = {}
        # for i in range(len(nums)):
        #     if nums[i] not in count:
        #         count[nums[i]] = 1
        #     else:
        #         count[nums[i]] += 1
        # return list(count.keys())[list(count.values()).index(max(list(count.values())))]