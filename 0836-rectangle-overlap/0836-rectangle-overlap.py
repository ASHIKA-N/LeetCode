class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        (x1,y1,x2,y2)=rec1
        (X1,Y1,X2,Y2)=rec2
        return x1<X2 and X1<x2 and y1<Y2 and Y1<y2