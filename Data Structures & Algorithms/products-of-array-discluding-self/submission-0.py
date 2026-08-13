class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        prefP = 1
        suff = [0] * n
        suffS = 1
        ret = [0] * n
        for i in range(len(nums)):
            pref[i] = prefP
            prefP *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            suff[i] = suffS
            suffS *= nums[i]

        for i in range(len(nums)):
            ret[i] = pref[i]*suff[i]

        return ret

        