class Solution {
		long get(int[] dr, int[] dc, int sr, int sc)
		{
			long ret = 1L<<sr*8+sc;
			for(int i = 0;i < dr.length;i++){
				int rr = dr[i], cc = dc[i];
				int r = sr, c = sc;
				while(r >= 0 && r < 8 && c >= 0 && c < 8){
					ret |= 1L<<r*8+c;
					r += rr; c += cc;
				}
			}
			return ret;
		}

		public int countCombinations(String[] pieces, int[][] positions) {
			int n = pieces.length;
			long[] ptns = new long[n];
			for(int i = 0;i < n;i++){
				if(pieces[i].equals("bishop")){
					ptns[i] = get(new int[]{-1, 1, -1, 1}, new int[]{-1, -1, 1, 1}, positions[i][0]-1,
							positions[i][1]-1);
				}else if(pieces[i].equals("rook")) {
					ptns[i] = get(new int[]{-1, 1, 0, 0}, new int[]{0, 0, -1, 1}, positions[i][0] - 1,
							positions[i][1] - 1);
				}else{
					ptns[i] = get(new int[]{-1, 1, -1, 1, -1, 1, 0, 0}, new int[]{-1, -1, 1, 1, 0, 0, -1, 1}, positions[i][0]-1,
							positions[i][1]-1);
				}
			}

			int[] a = new int[n];
			int ans = 0;
			outer:
			do{
				for(int i = 0;i < n;i++){
					if(ptns[i]<<~a[i]>=0)continue outer;
				}

				for(int t = 1;t < 8;t++){
					int[] rcs = new int[n];
					for(int i = 0;i < n;i++) {
						int gdr = (a[i] / 8) - (positions[i][0] - 1);
						int gdc = (a[i] % 8) - (positions[i][1] - 1);
						int mtime = Math.max(Math.abs(gdr), Math.abs(gdc));
						if(t <= mtime){
							rcs[i] = (positions[i][0] - 1 + gdr/mtime*t) * 8 +
									(positions[i][1] - 1 + gdc/mtime*t);
						}else{
							rcs[i] = a[i];
						}
					}
					for(int i = 0;i < n;i++){
						for(int j = i+1;j < n;j++){
							if(rcs[i] == rcs[j])continue outer;
						}
					}
				}

				ans++;
			}while(inc(a, 64));
			return ans;
		}

		public boolean inc(int[] a, int base)
		{
			int n = a.length;
			int i;
			for(i = n - 1;i >= 0 && a[i] == base - 1;i--);
			if(i == -1)return false;

			a[i]++;
			Arrays.fill(a, i + 1, n, 0);
			return true;
		}

	}
