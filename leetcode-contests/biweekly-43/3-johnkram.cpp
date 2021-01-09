class Solution {
    int m,a[50];
    vector<int> ans;
    bool b[25];
    bool dfs(int x)
    {
        int i;
        if(x+1==m<<1)
        {
            ans.clear();
            for(i=0;i+1<m<<1;i++)ans.push_back(a[i]);
            return 1;
        }
        if(a[x])return dfs(x+1);
        for(i=m;i>1;i--)if(!b[i]&&x+i+1<m<<1&&!a[x+i])
        {
            a[x]=a[x+i]=i;
            b[i]=1;
            if(dfs(x+1))return 1;
            a[x]=a[x+i]=b[i]=0;
        }
        if(!b[1])
        {
            a[x]=b[1]=1;
            if(dfs(x+1))return 1;
            a[x]=b[1]=0;
        }
        return 0;
    }
public:
    vector<int> constructDistancedSequence(int n) {
        m=n;
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        dfs(0);
        return ans;
    }
};