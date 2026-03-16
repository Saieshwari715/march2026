class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            j=0
            while j<len(str(i)):
                j+=1
            if j%2==0:
                c+=1
        return c

        