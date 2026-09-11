import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=[[]for _ in range(n)]
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        heap=[(0,0)]
        dist=[float('inf')]*(n)
        ways=[0]*n
        dist[0]=0
        ways[0]=1
        MOD=10**9+7
        while heap:
            dis,node=heapq.heappop(heap)
            if dis>dist[node]:
                continue
            for neigh,w in graph[node]:
                new_d=dis+w
                if new_d<dist[neigh]:
                    heapq.heappush(heap,(new_d,neigh))
                    dist[neigh]=new_d
                    ways[neigh]=ways[node]
                elif new_d==dist[neigh]:
                    ways[neigh]=(ways[neigh]+ways[node])%MOD
        
        return ways[n-1]