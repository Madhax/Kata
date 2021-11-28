	class Solution {
		public int networkBecomesIdle(int[][] edges, int[] patience) {
			int m = edges.length;
			int[] from = new int[m];
			int[] to = new int[m];
			for(int i = 0;i < m;i++){
				from[i] = edges[i][0];
				to[i] = edges[i][1];
			}
			int n = patience.length;
			int[][] g = packU(n, from, to);

			int[] ds = bfs(g, 0);
			int ans = 0;
			for(int i = 1;i < n;i++){
				int d = ds[i];
				int last = 2*d / patience[i] * patience[i];
				if(last == 2*d){
					last -= patience[i];
				}
				ans = Math.max(ans, last + 2*d + 1);
			}
			return ans;
		}

		public int[] bfs(int[][] g, int s)
		{
			int n = g.length;
			int[] q = new int[n];
			int[] ds = new int[n];
			Arrays.fill(ds, Integer.MAX_VALUE / 2);
			int qp = 0;
			q[qp++] = s;
			ds[s] = 0;
			for(int z = 0;z < qp;z++){
				int cur = q[z];
				for(int e : g[cur]){
					if(ds[e] > ds[cur] + 1){
						ds[e] = ds[cur] + 1;
						q[qp++] = e;
					}
				}
			}
			return ds;
		}


		public int[][] packU(int n, int[] from, int[] to) {
			return packU(n, from, to, from.length);
		}

		public int[][] packU(int n, int[] from, int[] to, int sup) {
			int[][] g = new int[n][];
			int[] p = new int[n];
			for (int i = 0; i < sup; i++) p[from[i]]++;
			for (int i = 0; i < sup; i++) p[to[i]]++;
			for (int i = 0; i < n; i++) g[i] = new int[p[i]];
			for (int i = 0; i < sup; i++) {
				g[from[i]][--p[from[i]]] = to[i];
				g[to[i]][--p[to[i]]] = from[i];
			}
			return g;
		}

	}
