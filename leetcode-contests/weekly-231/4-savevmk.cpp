class Solution {
    public int minChanges(int[] nums, int k) {
        int n = nums.length;
        int[][] dp = new int[k+1][1<<10];
        int[][] cts = new int[k][1<<10];
        ArrayList<HashSet<Integer>> hc = new ArrayList<>();
        for (int i = 0; i < k; ++i)
            hc.add(new HashSet<>());
        int[] tcs = new int[k];
        for (int i = 0; i < nums.length; ++i) {
            cts[i%k][nums[i]]++;
            tcs[i%k]++;
            hc.get(i%k).add(nums[i]);
        }
        dp[0][0] = 0;
        for (int i = 1; i < 1024; ++i)
            dp[0][i] = 1000000;
        for (int i = 0; i < k; ++i) {
            int min = 1000000;
            for (int j = 0; j < 1024; ++j)
                min = Math.min(min, dp[i][j]);
            for (int j = 0; j < 1024; ++j)
                dp[i+1][j] = min+tcs[i];
            for (int j2 : hc.get(i)) {
                for (int j = 0; j < 1024; ++j) {
                    dp[i+1][j^j2] = Math.min(dp[i+1][j^j2], dp[i][j]+tcs[i]-cts[i][j2]);
                }
            }
        }
        return dp[k][0];
    }
}
