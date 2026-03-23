class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        
        s=sum(nums[:k])
        maxi=s

        for i in range(k,n):
            s=s+nums[i]-nums[i-k]
        
            maxi=max(maxi,s)
        return maxi/k


        