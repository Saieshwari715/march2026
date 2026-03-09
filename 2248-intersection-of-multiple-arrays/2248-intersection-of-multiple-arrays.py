class Solution:
    def intersection(self, nums):
        d = {}
        
        for arr in nums:
            for num in arr:
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
        
        res = []
        for key in d:
            if d[key] == len(nums):
                res.append(key)
        
        return sorted(res)