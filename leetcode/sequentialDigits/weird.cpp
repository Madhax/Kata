class Solution {
public:
    bool findSeq(vector<int> &res, int l, int h, int c)
    {
        for(int i=1; i<=10-c; i++)
        {
            int num = 0;
            for(int j=i, k=0; j<10 && k<c; j++, k++)
            {
                num = num * 10 + j;
            }
            if(num > h)
                return true;
            if(num >= l)
                res.push_back(num);
        }
        return false;
    }
    vector<int> sequentialDigits(int low, int high) {
        int ll = to_string(low).size();
        int hl = to_string(high).size();
        vector<int> res;
        for(int i=ll; i<=hl; i++)
        {
            if(findSeq(res, low, high, i))
                return res;
        }
        return res;
    }
};