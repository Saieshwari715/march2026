from collections import deque,defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        outdegree=[0]*n
        reverse_graph=defaultdict(list)
        for u in range(n):
            outdegree[u]=len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)
        q=deque()
        for i in range(n):
            if outdegree[i]==0:
                q.append(i)
        safe=[]
        while q:
            node=q.popleft()
            safe.append(node)
            for parent in reverse_graph[node]:
                outdegree[parent]-=1
                if outdegree[parent]==0:
                    q.append(parent)
        return sorted(safe)



        
        