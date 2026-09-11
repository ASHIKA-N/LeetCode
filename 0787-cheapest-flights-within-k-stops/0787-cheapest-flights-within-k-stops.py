import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=[[]for _ in range(n)]
        for u,v,w in flights:
            graph[u].append((v,w))
        dist=[[float('inf')]*(k+2) for _ in range(n)]
        heap=[(0,src,0)]
        dist[src][0]=0
        ans=0
        while heap:
            d,node,stp=heapq.heappop(heap)
            if node==dst:
                return d
            if stp==k+1:
                continue
            for v,w in graph[node]:
                new_d=d+w
                new_stp=stp+1
                if new_d<dist[v][new_stp]:
                    heapq.heappush(heap,(new_d,v,new_stp))
                    dist[v][new_stp]=new_d
        return -1
                
            