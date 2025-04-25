class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[];
        d={']':'[','}':'{',')':'('}
        for i in s:
            if(i == '(' or i=='[' or i=='{'):
                st.append(i)
            elif(st):
                if(i==')' and st[-1]!='(' or i==']' and st[-1]!='[' or i=='}' and st[-1]!='{' ):
                    return False
                else:
                    st.pop()
            else:
                return False
        return len(st)==0
