import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost=0
        visited=[False]*len(points)
        pq=[(0,0)]
        while pq:
            cost,u=heapq.heappop(pq)
            if visited[u]:
                continue
            min_cost+=cost
            visited[u]=True
            for v in range(len(points)):
                if not visited[v]:
                    dist=abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])
                    heapq.heappush(pq,(dist,v))
        return min_cost
        
        
        