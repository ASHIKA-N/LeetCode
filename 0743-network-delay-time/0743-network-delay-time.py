import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[]for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append((v,w))
        heap=[(0,k)]
        dist=[float('inf')]*(n+1)
        dist[k]=0
        while heap:
            dis,node=heapq.heappop(heap)
            if dis>dist[node]:
                continue
            for neigh,w in graph[node]:
                new_d=dis+w
                if new_d<dist[neigh]:
                    heapq.heappush(heap,(new_d,neigh))
                    dist[neigh]=new_d
            ans=0
        for i in range(1,n+1):
            if dist[i]==float('inf'):
                return -1
            ans=max(ans,dist[i])
        return ans



