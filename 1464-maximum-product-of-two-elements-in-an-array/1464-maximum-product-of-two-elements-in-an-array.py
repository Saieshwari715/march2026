class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i=0
        maxi=0
        while i<len(nums):
            for j in range(1,len(nums)):
                if i!=j:
                    mul=(nums[i]-1)*(nums[j]-1)
                    maxi=max(maxi,mul)
            i+=1
        return maxi
        
        