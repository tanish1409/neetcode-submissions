class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.replace(" ", "") 
        sf = s.lower()
        s = "".join(char for char in sf if char.isalnum())
        print(s)
        i = 0
        j = len(s) - 1
        flag = True

        while i<j:
            if s[i] == s[j]:
                i +=1
                j -=1
            else:
                flag = False
                break

        return flag

        