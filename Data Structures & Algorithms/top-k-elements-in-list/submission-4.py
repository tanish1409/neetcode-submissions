class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        ret = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] +=1
        #print(seen)

        lis = list(seen.keys())
        lis.sort(key=seen.get, reverse=True)
        return lis[:k]
        