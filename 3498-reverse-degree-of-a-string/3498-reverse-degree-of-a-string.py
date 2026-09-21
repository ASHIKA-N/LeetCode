class Solution:
    def reverseDegree(self, s: str) -> int:
        num=0
        for i in range(len(s)):
            print(ord(s[i]))
            num+=(ord('z')-ord(s[i])+1)*(i+1)
        return num
        