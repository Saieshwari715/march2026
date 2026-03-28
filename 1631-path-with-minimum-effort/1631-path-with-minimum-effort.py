class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        dist=[[float('inf')]*m for _ in range(n)]
        directions=[(0,-1),(1,0),(-1,0),(0,1)]
        dist[0][0]=0
        heap=[(0,0,0)]
        
        
        while heap:
            diff,sr,sc=heapq.heappop(heap)
            if sr==n-1 and sc==m-1:
                return diff
            for i,j in directions:
                nr,nc=sr+i,sc+j
                if 0<=nr<n and 0<=nc<m:
                    effort=abs(heights[sr][sc]-heights[nr][nc])
                    new_diff=max(diff,effort)
                    if dist[nr][nc]>new_diff:
                        dist[nr][nc]=new_diff
                        heapq.heappush(heap,(new_diff,nr,nc))
        return 0

                




        
        