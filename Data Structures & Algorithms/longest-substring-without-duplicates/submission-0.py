class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i ,j = 0, 0
        res = 0
        charSet = set()
        for j in range(len(s)):
            while s[j] in charSet:
                charSet.remove(s[i])
                i +=1
            charSet.add(s[j])
            res = max(res, j-i+1)
        return res



        