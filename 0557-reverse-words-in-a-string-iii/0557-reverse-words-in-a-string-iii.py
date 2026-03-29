class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        st=[]
        for i in w:
            st.append(i[::-1])
        return " ".join(st)
        