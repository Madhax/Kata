	class Solution {
		public long kthSmallestProduct(int[] nums1, int[] nums2, long k) {
			long[] u = new long[nums2.length];
			for(int i = 0;i < nums2.length;i++){
				u[i] = nums2[i];
			}
			long low = -(long)2e10, high = (long)2e10;
			while(high - low > 1){
				long h = high+low>>1;
				long num = 0;
				for(int v : nums1){
					if(v > 0){
						int lb = lowerBound(u, Math.floorDiv(h, v) + 1);
						num += lb;
					}else if(v < 0){
						long o = Math.floorDiv(h+v+1, v);
						int lb = lowerBound(u, o);
						num += u.length-lb;
					}else{
						if(h >= 0){
							num += u.length;
						}
					}
				}
				if(num >= k){
					high = h;
				}else{
					low = h;
				}
			}
			return high;
		}

		public int lowerBound(long[] a, long v)
		{
			int low = -1, high = a.length;
			while(high-low > 1){
				int h = high+low>>>1;
				if(a[h] >= v){
					high = h;
				}else{
					low = h;
				}
			}
			return high;
		}

	}
