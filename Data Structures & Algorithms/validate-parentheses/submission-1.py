from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        flag = True
        st = deque()
        if s == "":
            return flag
        if len(s) == 1:
            return False
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                st.append(c)
            if (c == ')'):
                if st[-1] == '(':
                    st.pop()    
                else:
                    flag = False
            if (c == ']'):
                if st[-1] == '[':
                    st.pop()    
                else:
                    flag = False
            if (c == '}'):
                if st[-1] == '{':
                    st.pop()    
                else:
                    flag = False

        return flag
            
