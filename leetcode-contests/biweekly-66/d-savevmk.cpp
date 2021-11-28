class Solution {
    public int countPyramids(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] last = new int[n][m];
        for (int i = 0; i < n; ++i) {
            last[i][m-1] = m-2+grid[i][m-1];
            for (int j = m-2; j >= 0; --j) {
                last[i][j] = j-1;
                if (grid[i][j]==1)
                    last[i][j] = last[i][j+1];
            }
        }
        int ans = 0;
        for (int i = 0; i < n-1; ++i) {
            for (int j = 1; j < m-1; ++j) {
                if (grid[i][j]==0)
                    continue;
                for (int k = 1; i+k<n&&j-k>=0&&j+k<m; ++k) {
                    if (last[i+k][j-k]<j+k)
                        break;
                    ++ans;
                }
            }
        }
        for (int i = n-1; i > 0; --i) {
            for (int j = 1; j < m-1; ++j) {
                if (grid[i][j]==0)
                    continue;
                for (int k = 1; i-k>=0&&j-k>=0&&j+k<m; ++k) {
                    if (last[i-k][j-k]<j+k)
                        break;
                    ++ans;
                }
            }
        }
        return ans;
    }
}
