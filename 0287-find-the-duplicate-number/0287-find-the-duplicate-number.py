class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        hash={}
        for i in nums:
            '''if i in hash:
                return i
                break
            else:
                hash[i]=1'''

            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for key,value in hash.items():
            if value>1:
                return key
                break

    