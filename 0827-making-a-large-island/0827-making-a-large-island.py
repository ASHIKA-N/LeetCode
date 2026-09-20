class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        dr=[(-1,0),(1,0),(0,-1),(0,1)]
        n=len(grid)
        m=len(grid[0])
        par=[x for x in range(n*m)]
        rank=[1]*(n*m)
        def find(n):
            p=par[n]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        def union(a,b):
            p1=find(a)
            p2=find(b)
            if p1==p2:
                return False
            elif rank[p1]>rank[p2]:
                rank[p1]+=rank[p2]
                par[p2]=p1
            else:
                rank[p2]+=rank[p1]
                par[p1]=p2
            return True
        for r in range(n):
            for c in range(m):
                if grid[r][c]==1:
                    for row,col in dr:
                        nr=r+row
                        nc=c+col
                        if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                            union(r*m+c,nr*m+nc)
        
        ans = max(rank) if any(any(row) for row in grid) else 0
        for r in range(n):
            for c in range(m):
                if grid[r][c]==0:
                    uniq=set()
                    for row,col in dr:
                        nr=r+row
                        nc=c+col
                        if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                            uniq.add(find(nr*m+nc))
                    ans = max(ans, 1 + sum(rank[root] for root in uniq))
        return ans if ans>0 else 1