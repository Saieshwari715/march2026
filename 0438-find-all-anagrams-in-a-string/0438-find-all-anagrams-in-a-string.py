class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        '''res=[]
        k=len(p)
        for i in range(len(s)-k+1):
            if sorted(p)==sorted(s[i:i+k]):
                res.append(i)
        return res'''

















        r=[]
        p_sorted=sorted(p)
        k=len(p)
        for i  in range(len(s)-k+1):
            if(sorted(s[i:i+k])==p_sorted):
                r.append(i)
        return r
        

