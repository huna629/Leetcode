class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        climb=[0]*(n+1)
        climb[0]=0
        climb[1]=1
        climb[2]=2
        
        for i in range(3, n+1):
            climb[i]=climb[i-1]+climb[i-2]
        
        return climb[n]
        