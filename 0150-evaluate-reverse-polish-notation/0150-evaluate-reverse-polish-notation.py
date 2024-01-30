class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        op={'+','-','*','/'}
        0
        for t in tokens:
            if t in op:
                a=st.pop()
                b=st.pop()
                if t =='+':
                    st.append(a+b)
                elif t=='-':
                    st.append(b-a)
                elif t=='*':
                    st.append(a*b)
                elif t=='/':
                    st.append(int(b/a))
            else:
                st.append(int(t))
        return st[0]