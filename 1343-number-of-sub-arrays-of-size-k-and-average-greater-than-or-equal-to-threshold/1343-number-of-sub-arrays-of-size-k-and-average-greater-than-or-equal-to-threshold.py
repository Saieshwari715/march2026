class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        c=0
        s=sum(arr[:k])
        avg=s//k
        if avg>=threshold:
            c+=1
        for i in range(k,n):
            s=s+arr[i]-arr[i-k]
            avg=s//k
            if avg>=threshold:
                c+=1
        return c
        

        