class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res, count = [], {}
        buckets = [[] for x in range(len(nums)+1)]
        
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
            
        for key in count:
            buckets[count[key]].append(key)
            
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res