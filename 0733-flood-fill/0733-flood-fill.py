class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols=len(image),len(image[0])
       
        if image[sr][sc]==color:
            return image

        q=deque()
        q.append((sr,sc))
        val=image[sr][sc]
        dir=[(0,-1),(1,0),(0,1),(-1,0)]
        while q:
            r,c=q.popleft()
            image[r][c]=color
            for i,j in dir:
                nr,nc=i+r,j+c
                if nr>=0 and nr<rows and nc>=0 and nc<cols:
                    if image[nr][nc]==val:
                        image[nr][nc]=color
                        q.append((nr,nc))
        return image


































        '''original=image[sr][sc]
        rows,cols=len(image),len(image[0])
        if original==color:
            return image
        rows,cols=len(image),len(image[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=original:
                return 
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image'''















        
        
        
        
        '''original=image[sr][sc]
        rows,cols=len(image),len(image[0])
        if original==color:
            return image
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=original:
                return 
            image[r][c]=color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image'''


        