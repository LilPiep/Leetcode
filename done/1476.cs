public class SubrectangleQueries {

    int[][] ans;

    public SubrectangleQueries(int[][] rectangle) {
        ans = rectangle;
    }
    
    public void UpdateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        for(int i=row1;i<=row2;i++){
            for(int j=col1;j<=col2;j++){
                ans[i][j]=newValue;
            }
        }
    }
    
    public int GetValue(int row, int col) {
        return ans[row][col];
    }
}

/**
 * Your SubrectangleQueries object will be instantiated and called as such:
 * SubrectangleQueries obj = new SubrectangleQueries(rectangle);
 * obj.UpdateSubrectangle(row1,col1,row2,col2,newValue);
 * int param_2 = obj.GetValue(row,col);
 */