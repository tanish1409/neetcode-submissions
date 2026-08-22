class Solution:
    def helper(self, nums: list[int]):

        rob1,rob2 = 0, 0
        for n in nums:
            newrob = max(rob1, rob2 +n)
            rob2 = rob1
            rob1 = newrob

        return rob1
    
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))