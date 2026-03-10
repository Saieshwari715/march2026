class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxi=-1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    d=nums[j]-nums[i]
                    maxi=max(maxi,d)
        return maxi

        

        