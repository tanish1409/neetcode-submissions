class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand(l:int, r:int) -> str:
            local_count = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                local_count +=1
                l -=1
                r +=1
            return local_count
        
        for i in range(len(s)):
            count += expand(i,i)

            count += expand(i,i+1)

        return count
        