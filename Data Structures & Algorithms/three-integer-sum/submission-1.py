class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == 0:
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                if threesum > 0:
                    k -= 1
                if threesum < 0:
                    j +=1
        return ret


        