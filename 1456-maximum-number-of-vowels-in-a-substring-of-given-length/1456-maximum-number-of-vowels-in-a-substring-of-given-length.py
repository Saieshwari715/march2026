class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        maxi=0
        c=0
        for i in range(k):
            if s[i] in v:
                c+=1
        maxi=c
        for i in range(k,len(s)):
            if s[i] in v:
                c+=1
            if s[i-k] in v:
                c-=1
            maxi=max(maxi,c)
        return maxi

        '''i=0

        while i<=len(s)-k:
            t=s[i:k+i]
            c=0
            for j in t:
                if j in v:
                    c+=1

            maxi=max(maxi,c)
            i+=1
        return maxi
'''
        