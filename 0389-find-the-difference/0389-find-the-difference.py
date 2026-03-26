class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t_s=0
        s_s=0
        t=sorted(t)
        for i in s:
            s_s+=ord(i)
        for i in t:
            t_s+=ord(i)
        diff=abs(s_s-t_s)
        return chr(diff)
            
