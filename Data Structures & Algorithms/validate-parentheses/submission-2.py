from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        flag = True
        st = deque()
        if s == "":
            return flag
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                st.append(c)
            if (c == ')'):
                if st and st[-1] == '(':
                    st.pop()    
                else:
                    flag = False
            if (c == ']'):
                if st and st[-1] == '[':
                    st.pop()    
                else:
                    flag = False
            if (c == '}'):
                if st and st[-1] == '{':
                    st.pop()    
                else:
                    flag = False

        if len(st) != 0:
            flag=False

        return flag
            
