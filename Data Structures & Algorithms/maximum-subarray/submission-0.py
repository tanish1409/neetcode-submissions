class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxs = nums[0]
        suml = 0

        for num in nums:
            if suml < 0:
                suml = 0
            suml += num
            maxs = max(maxs,suml)

        return maxs
