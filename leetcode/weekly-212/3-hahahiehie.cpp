class Solution {
    private static final int INF = 1_000_000_001;
    private static final long MOD = 1_000_000_007;
    private static final int UNSET = -123;
    private static final int[][] DIR = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    int[][] heights;

    public int minimumEffortPath(int[][] heights) {
        this.heights = heights;
        int m = heights.length;
        int n = heights[0].length;

        int ans = 0;
        int low = 0;
        int high = 1000000 + 10;
        while (low <= high) {
            int mid = (low + high) / 2;
            boolean[][] vst = new boolean[m][n];
            if (dfs(0, 0, mid, vst)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    boolean dfs(int x, int y, int maxDiff, boolean[][] vst) {
        int m = heights.length;
        int n = heights[0].length;
        if (x == m - 1 && y == n - 1) return true;

        if (vst[x][y]) return false;

        vst[x][y] = true;
        for (int i = 0; i < DIR.length; i++) {
            int nx = x + DIR[i][0];
            int ny = y + DIR[i][1];
            if (!(nx >= 0 && nx < m && ny >= 0 && ny < n)) continue;
            if (vst[nx][ny]) continue;

            int diff = Math.abs(heights[nx][ny] - heights[x][y]);
            if (diff > maxDiff) continue;
            if (dfs(nx, ny, maxDiff, vst)) return true;
        }
        return false;
    }
}