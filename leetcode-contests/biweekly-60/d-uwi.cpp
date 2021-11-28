class Solution {
    public int numberOfGoodSubsets(int[] nums) {
        int[] f = new int[31];
        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
        for(int v : nums){
            f[v]++;
        }
        boolean[] ng = new boolean[31];
        int[] ptn = new int[31];
        outer:
        for(int i = 1;i <= 30;i++){
            int x = i;
            int k = 0;
            for(int p : primes){
                int e = 0;
                while(x % p == 0){
                    x /= p;
                    e++;
                }
                if(e >= 2){
                    ng[i] = true;
                    continue outer;
                }
                if(e == 1){
                    ptn[i] |= 1<<k;
                }
                k++;
            }
        }
        long[] g = new long[1<<11];
        final int mod = 1000000007;
        g[0] = 1;
        for(int i = 2;i <= 30;i++){
            if(ng[i])continue;
            long t = f[i];
            for(int j = 0;j < 1<<11;j++){
                if((j&ptn[i]) == 0){
                    g[j|ptn[i]] += g[j] * t;
                    g[j|ptn[i]] %= mod;
                }
            }
        }
        long ans = 0;
        for(int i = 1;i < 1<<11;i++){
            ans += g[i];
        }
        ans = ans % mod * pow(2, f[1], mod) % mod;
        return (int)(ans%mod);
    }
    
    
	public long pow(long a, long n, long mod) {
		//		a %= mod;
		long ret = 1;
		int x = 63 - Long.numberOfLeadingZeros(n);
		for (; x >= 0; x--) {
			ret = ret * ret % mod;
			if (n << 63 - x < 0) ret = ret * a % mod;
		}
		return ret;
	}

}
