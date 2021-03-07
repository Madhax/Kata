class Solution {
    public int[] countPairs(int n, int[][] es, int[] qs) {
        int[] cts = new int[n];
        ArrayList<HashMap<Integer, Integer>> alhm = new ArrayList<>();
        for (int i = 0; i < n; ++i)
            alhm.add(new HashMap<>());
        for (int[] e : es) {
            cts[e[0]-1]++;
            cts[e[1]-1]++;
            int u = Math.min(e[0]-1,e[1]-1);
            int v = Math.max(e[0]-1,e[1]-1);
            if (!alhm.get(u).containsKey(v))
                alhm.get(u).put(v,1);
            else
                alhm.get(u).put(v,alhm.get(u).get(v)+1);
        }
        int[] rcs = new int[es.length+2];
        for (int i = 0; i < n; ++i) {
            rcs[cts[i]]++;
        }
        int[] rcsal = new int[es.length+2];
        for (int i = es.length; i>=0; --i) {
            rcsal[i] = rcsal[i+1]+rcs[i];
        }
        int[] drop = new int[es.length*2+2];
        for (int[] e : es) {
            int u = Math.min(e[0]-1,e[1]-1);
            int v = Math.max(e[0]-1,e[1]-1);
            if (alhm.get(u).containsKey(v)) {
                int val = alhm.get(u).get(v);
                for (int i = 0; i < val; ++i) {
                    drop[cts[u]+cts[v]-i]--;
                }
                alhm.get(u).remove(v);
            }
        }
        int[] ans = new int[qs.length];
        for (int i = 0; i < qs.length; ++i) {
            int q = qs[i];
            ans[i] = drop[q+1];
            //System.out.println(i+" "+ans[i]);
            for (int j = 0; j <= es.length; ++j) {
                int k = q+1-j;
                if (k<j)
                    k=j;
                if (j==k) {
                    ans[i] += rcs[j]*(rcs[j]-1)/2;
                    ++k;
                }
                ans[i] += rcs[j]*rcsal[k];
                //System.out.println(i+" "+j+" "+ans[i]);
            }
        }
        return ans;
    }
}
