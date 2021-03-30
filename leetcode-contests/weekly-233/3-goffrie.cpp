#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#pragma GCC optimize("Ofast")
#define min(x,y) ({ __typeof__(x) __var0 = (x); __typeof__(y) __var1 = (y); __var0 < __var1 ? __var0 : __var1; })
#define max(x,y) ({ __typeof__(x) __var0 = (x); __typeof__(y) __var1 = (y); __var0 < __var1 ? __var1 : __var0; })
#define abs(x) ({ __typeof__(x) __var = (x); __var < 0 ? -__var : __var; })
#define sumvn(v, n) ({ __typeof__(v[0]) __ans = 0; __typeof__(&v[0]) __p = &v[0]; for (size_t __i = 0, __len = (n); __i < __len; ++__i) __ans += __p[__i]; __ans; })
#define sumv(v) sumvn(v, (v).size())
#define maxvn(v, n) ({ __typeof__(&v[0]) __p = &v[0]; __typeof__(v[0]) __ans = __p[0]; for (size_t __i = 1, __len = (n); __i < __len; ++__i) if (__p[__i] > __ans) __ans = __p[__i]; __ans; })
#define maxv(v) maxvn(v, (v).size())
#define minvn(v, n) ({ __typeof__(&v[0]) __p = &v[0]; __typeof__(v[0]) __ans = __p[0]; for (size_t __i = 1, __len = (n); __i < __len; ++__i) if (__p[__i] < __ans) __ans = __p[__i]; __ans; })
#define minv(v) minvn(v, (v).size())
#define prefix_sumvn(v, n) ({ __typeof__(&v[0]) __p = &v[0]; for (size_t __i = 1, __len = (n); __i < __len; ++__i) __p[__i] += __p[__i-1]; })
#define prefix_sumv(v, n) prefix_sumvn(v, (v).size())
#define sumrange(v, i, j) ({ size_t __i = i, __j = j; (__j ? v[__j - 1] : 0) - (__i ? v[__i - 1] : 0); })
#define splitv(v, n, w) int n = (w).size(); auto v = &w[0];

#define MP make_pair
#define MT make_tuple
#define all(v) (v).begin(), (v).end()
// in bounds
#define IB(x, n) ((x) >= 0 && (x) < (n))
#define IB2(x, y, n, m) (IB(x, n) && IB(y, m))
// neighbours
#define N4(i, j) ((pair<int,int>[]){{(i)-1,(j)},{(i)+1,(j)},{(i),(j)-1},{(i),(j)+1}})
#define N8(i, j) ((pair<int,int>[]){{(i)-1,(j)},{(i)+1,(j)},{(i),(j)-1},{(i),(j)+1},{(i)-1,(j)-1},{(i)+1,(j)-1},{(i)-1,(j)+1},{(i)+1,(j)+1}})
// iterate neighbours
#define F4(i2, j2, i, j, n, m) for (auto [i2, j2]: N4(i, j)) if (IB2(i2, j2, n, m))
#define F8(i2, j2, i, j, n, m) for (auto [i2, j2]: N8(i, j)) if (IB2(i2, j2, n, m))
// debugging
#define DBG(x) cerr << #x << "=" << (x) << endl;
#define CONTAINER(TY) template<typename T> ostream& operator<<(ostream& os, const TY<T>& v) { os << "["; bool f = true; for (const T& x: v) { if (!f) os << ","; os << x; f = 0; } return os << "]"; }
CONTAINER(vector)
CONTAINER(set)
CONTAINER(multiset)
CONTAINER(unordered_set)
CONTAINER(unordered_multiset)
#define CONTAINER2(TY) template<typename T, typename U> ostream& operator<<(ostream& os, const TY<T, U>& v) { os << "{"; bool f = true; for (const auto& x: v) { if (!f) os << ","; os << x.first << ':' << x.second; f = 0; } return os << "}"; }
CONTAINER2(map)
CONTAINER2(multimap)
CONTAINER2(unordered_map)
template<typename T, typename U> ostream& operator<<(ostream& os, const pair<T, U>& v) { return os << "(" << v.first << "," << v.second << ")"; }
template<int I, typename T> struct Ptuple { static void print(ostream& os, const T& v) { Ptuple<I-1, T>::print(os, v); if (I > 1) os << ","; os << get<I-1>(v); } };
template<typename T> struct Ptuple<0, T> { static void print(ostream& os, const T& v) { } };
template<typename... T> ostream& operator<<(ostream& os, const tuple<T...>& v) { return os << "(", Ptuple<tuple_size<tuple<T...>>::value, tuple<T...>>::print(os, v), os << ")"; }
const int _fast_io = []() { ios::sync_with_stdio(false); cin.tie(0); cout.tie(0); return 0; }();
class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        auto tri = [&](ll v, ll m) {
            if (m <= v) {
                ll first = v;
                ll last = v-m+1;
                return (first+last)*m/2;
            } else {
                ll first = v;
                ll last = 1;
                return (first+1)*v/2 + (m-v);
            }
        };
        auto can = [&](ll v) {
            ll sum = v + tri(max(1,v-1), n-index-1) + tri(max(1,v-1), index);
            return sum <= maxSum;
        };
        ll lo = 1, hi = maxSum+1;
        while (lo<hi-1) {
            ll mid = (lo+hi)/2;
            if (can(mid)) lo=mid;
            else hi=mid;
        }
        return lo;
    }
};
