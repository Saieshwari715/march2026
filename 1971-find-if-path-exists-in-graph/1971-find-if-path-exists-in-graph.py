from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], sr: int, destination: int) -> bool:
        graph=defaultdict(list)
        visited=[False]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q=deque()
        q.append(sr)
        visited[sr]=True
        while q:
            node=q.popleft()
            if visited[destination]:
                return True
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei]=True
                    q.append(nei)
        return False
                





        