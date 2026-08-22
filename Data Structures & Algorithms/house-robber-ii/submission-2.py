class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n ==1:
            return nums[0]
        cache = [[-1]*2 for i in range(n)]
        def dfs(i, flag):

            if i>= n or (flag and i == n-1):
                return 0
            
            if cache[i][flag] != -1:
                return cache[i][flag]

            cache[i][flag] = max(dfs(i+1, flag), dfs(i+2, flag)+nums[i])
            return cache[i][flag]

        return max(dfs(0, True), dfs(1,False))