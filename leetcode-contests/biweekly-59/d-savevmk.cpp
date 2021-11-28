class Solution {
    public int numberOfCombinations(String num) {
        if (num.charAt(0)=='0')
            return 0;
        int n = num.length();
        int[][] dp = new int[n][n];
        int[][] dpo = new int[n][n];
        boolean[][] eq10 = new boolean[n][n];
        boolean[][] eq100 = new boolean[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = i+10; j+10<n; ++j) {
                eq10[i][j] = true;
                for (int k = 0; k < 10; ++k) {
                    if (num.charAt(i+k)!=num.charAt(j+k)) {
                        eq10[i][j] = false;
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = i+100; j+100<n; ++j) {
                eq100[i][j] = true;
                for (int k = 0; k < 100; k+=10) {
                    if (!eq10[i+k][j+k]) {
                        eq100[i][j] = false;
                        break;
                    }
                }
            }
        }
        dp[0][0] = 1;
        dpo[0][0] = 1;
        for (int i = 1; i < num.length(); ++i) {
            if (num.charAt(i)>=num.charAt(i-1)) {
                dp[i][i] = dp[i-1][i-1];
                dpo[i][i] = dpo[i-1][i-1];
            }
        }
        for (int z = 1; z < n; ++z) {
            for (int i = 0; i < n; ++i) {
                int j = i+z;
                if (i==0) {
                    dpo[i][j] = 1;
                    dp[i][j] = (dp[i+1][j]+dpo[i][j])%1000000007;
                    continue;
                }
                if (j>=n)
                    break;
                if (num.charAt(i)=='0') {
                    dp[i][j] = (dp[i+1][j]+dpo[i][j])%1000000007;
                    continue;
                }
                int jm = Math.max(-1,i-z-1);
                dpo[i][j] = dp[jm+1][i-1];
                if (jm>=0) {
                    boolean add = true;
                    for (int k = 0; k <= z; ++k) {
                        if (eq100[jm+k][i+k]) {
                            k += 100;
                            continue;
                        }
                        if (eq10[jm+k][i+k]) {
                            k += 10;
                            continue;
                        }
                        if (num.charAt(jm+k)>num.charAt(i+k))
                            add = false;
                        if (num.charAt(jm+k)!=num.charAt(i+k))
                            break;
                    }
                    if (add) {
                        dpo[i][j] = (dpo[i][j]+dpo[jm][i-1])%1000000007;
                    }
                }
                dp[i][j] = (dp[i+1][j]+dpo[i][j])%1000000007;
            }
        }
        return dp[0][n-1];
    }
}
