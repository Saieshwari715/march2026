class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        maxi=0
        index=0
        for row in range(m):
            c=mat[row].count(1)
            if max(c, maxi) != maxi:
                maxi=max(c,maxi)
                index=row
        return [index,maxi]
        