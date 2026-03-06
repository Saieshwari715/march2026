class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    
    
        nums.sort(key=lambda x:(d[x],-x))
        return nums
        
        