class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fin = 1
        ret = 1
        nset = set(nums)
        arr = list(nset)
        arr.sort()
        i , j = 0, 1
        while j < len(arr):
            if arr[j] == arr[j-1] + +1:
                ret += 1
                j +=1
            else:
                fin = max(ret,fin)
                i = j
                j = i+1

        return max(ret,fin)
                

            
            

        