class NumMatrix {
    public static int[][] matrix;
    public NumMatrix(int[][] matrix) {
        this.matrix = matrix;    
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int ans = 0;
        for(int r=row1; r<=row2; r++){
            for(int c=col1; c<=col2; c++){
                ans+=this.matrix[r][c];
            }
        }
        return ans;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */