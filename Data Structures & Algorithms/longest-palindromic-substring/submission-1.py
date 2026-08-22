class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        res = ""

        def expand(l:int , r:int) -> str:
            while l>=0 and r<len(s) and s[l] == s[r]:
                l -=1
                r +=1

            return s[l+1:r]

        for i in range(len(s)):

            odd_str = expand(i,i)
            if len(odd_str) > len(res):
                res = odd_str
            
            even_str = expand(i,i+1)
            if len(even_str) > len(res):
                res = even_str

        return res

        



        