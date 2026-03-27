class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums))<3:
            return max(nums)        
        m1=float('-inf')
        m2=float('-inf')
        m3=float('-inf')
        nums=set(nums)
        for i in nums:
            if i>m1:
                m3=m2
                
                m2=m1
                m1=i
            elif i>m2 and i!=m1:
                m3=m2
                m2=i
            elif i>m3 and i!=m2 and i!=m3:
                m3=i
        return m3
                