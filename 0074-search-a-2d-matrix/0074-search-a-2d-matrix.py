class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:      
        if len(matrix[0])==1 and len(matrix)==1:
            if matrix[0][0]==target:
                return True
            else:
                return False
            
        for i in range(0, len(matrix)):
            if matrix[i][-1] >= target:
                low = 0
                high = len(matrix[0])
                while low<=high:
                    mid = (low+high)//2
                    if matrix[i][mid]==target:
                        return True
                    if matrix[i][mid]>target:
                        high = mid-1
                    else:
                        low= mid+1
                
            if matrix[i][0]>target:
                return False
                
            
[]