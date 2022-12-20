class Solution:
    def tribonacci(self, n: int) -> int:
        T1 = 0
        T2 = 1
        T3 = 1
        curr = 0
        if n<3:
            if n==0:
                return 0
            else:
                return 1
        for i in range(3, n+1):
            curr = T1+T2+T3
            T1=T2
            T2=T3
            T3=curr
            # print(curr)
        return curr