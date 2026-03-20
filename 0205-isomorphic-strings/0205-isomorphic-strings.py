class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        so={}
        to={}
        for i in range(len(s)):
            if s[i] not in so:
                so[s[i]]=i
            if t[i] not in to:
                to[t[i]]=i
            if so[s[i]]!=to[t[i]]:
                return False
        return True

        