class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch!=']':
                st.append(ch)
            else:
                temp=""
                while st and st[-1]!='[':
                    temp=st.pop()+temp
                st.pop()
                num=""
                while st and st[-1].isdigit():
                    num=st.pop()+num
                
                m=temp*int(num)
                st.append(m)
        return "".join(st)


        