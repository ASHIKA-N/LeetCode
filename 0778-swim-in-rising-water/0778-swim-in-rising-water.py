import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[(grid[0][0],0,0)]
        dr=[(-1,0),(1,0),(0,-1),(0,1)]
        visited={(0,0)}
        while heap:
            t,r,c=heapq.heappop(heap)
            if r==len(grid)-1 and c==len(grid[0])-1:
                return t
            for row,col in dr:
                nr=r+row
                nc=c+col
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited:
                    nt=max(t,grid[nr][nc]) 
                    heapq.heappush(heap,(nt,nr,nc))
                    visited.add((nr,nc))
                          
        return -1



