class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        string zigzags[numRows];
        
        bool goingDown = true;
        for(int iter, level = 0; iter < s.length(); iter++) {
            zigzags[level] += s[iter];
            if(goingDown) {
                level++;
                if(level==(numRows-1)) goingDown=false;
            }
            else {
                level--;
                if(level==0) goingDown=true;
            }
        }
        string response;
        for(int iter = 0; iter < numRows; iter++)
        {
            response+=zigzags[iter];
        }
        return response;
    }
};