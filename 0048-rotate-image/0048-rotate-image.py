class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        
        #REVERSE
        r = len(matrix)-1
        l = 0
        while l<r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l+=1
            r-=1
            
        #TRANSPOSE
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
