class Solution {
public:
    int f[1005];
    int Max[1005];
    int Find(int x){
        if(f[x]==x)return x;
        return f[x]=Find(f[x]);
    }
    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        vector<vector<int> > ans(matrix.size(),vector<int>(matrix[0].size()));
        map<int,vector<pair<int,int>> > m;
        for(int i = 0;i<matrix.size();i++){
            for(int j = 0;j<matrix[0].size();j++){
                m[matrix[i][j]].push_back(make_pair(i,j));
            }
        }
        int col[505],row[505];
        fill(col,col+505,0);
        fill(row,row+505,0);
        int n=matrix.size();
        for(auto &it:m){
            for(auto &it2:it.second){
                f[it2.first]=it2.first;
                Max[it2.first]=row[it2.first];
                f[it2.second+n]=it2.second+n;
                Max[it2.second+n]=col[it2.second];
            }
            for(auto &it2:it.second){
                int a=Find(it2.first),b=Find(it2.second+n);
                if(a!=b){
                    f[a]=b;
                    Max[b]=max(Max[b],Max[a]);
                }
            }
            for(auto it2:it.second){
                ans[it2.first][it2.second]=Max[Find(it2.first)]+1;
                row[it2.first]=col[it2.second]=ans[it2.first][it2.second];
            }
        }
        return ans;
    }
};