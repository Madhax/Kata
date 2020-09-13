class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows <= 1)
            return s;

        string z;
        z.resize(s.size());

        int j = 0;
        
        int stride = numRows + numRows - 2;
        for (int r = 0; r < numRows; ++r)
        {
            for (int i = r; i < s.size(); i += stride)
            {
                z[j++] = s[i];

                if (r > 0 && r < numRows - 1)
                {
                    int ii = i + (numRows - r - 1) * 2;
                    if(ii < s.size())
                        z[j++] = s[ii];
                }
            }
        }

        return z;
    }
};