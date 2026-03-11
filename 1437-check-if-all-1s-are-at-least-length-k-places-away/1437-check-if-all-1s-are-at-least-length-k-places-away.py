class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l=-1
        n=len(nums)
        f=True
        for r in range(n):
            if nums[r]==1:
                if l!=-1 and r-l-1<k:
                    f=False
                    break
                l=r
        return f


        
        
        