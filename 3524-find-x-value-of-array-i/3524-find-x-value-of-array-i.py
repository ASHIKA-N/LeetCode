class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp=[0]*k
        res=[0]*k
        for num in nums:
            new_dp=[0]*k
            new_dp[num%k]+=1
            for r in range(k):
                new_r=(r*num)%k
                new_dp[new_r]+=dp[r]
            dp=new_dp
            for r in range(k):
                res[r]+=dp[r]
        return res