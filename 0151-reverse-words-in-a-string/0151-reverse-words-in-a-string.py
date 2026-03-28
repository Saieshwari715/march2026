class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        t=words[::-1]
        '''left,right=0,len(words)-1
        while left<right:
            words[left],words[right]=words[right],words[left]
            left+=1
            right-=1'''
        return " ".join(t)

        