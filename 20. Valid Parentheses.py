class Solution(object):
    def isValid(self, s):
        st=[0]
        for x in s:
            if x=='{' or x=='(' or x=='[':
                st.append(x)
            elif x==')' and st[-1]=='(' or x==']' and st[-1]=='[' or x=='}' and st[-1]=='{':
                st.pop()
            else:
                return False

        if st[-1]==0:
            return True
        else:
            return False