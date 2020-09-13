class Solution {
public:
    string longestPalindrome(string s) {
        const char * iterator, *start = s.c_str();
        unsigned int offset = 0;
        char * longestFound;
        unsigned int sizeFound = 0;
        //
        while(offset < s.length()) 
        {
            bool isPalindrome = true;
            //check for centred
            unsigned int left, right = 0;
            for(int x = 0; (offset-x) >= 0 && offset+x < s.length(); x++) 
            {
                if(*(start-x+offset) != *(start+x+offset))
                    break;
                
                if(((x)*2+1) > sizeFound) {
                    longestFound = (char *)(start-x+offset);
                    sizeFound = (x*2+1);
                }
            }
            
            //check for lvalue
            for(int x = 0; (offset-x) >= 0 && offset+x < s.length()-1; x++) 
            {
                cout << offset << " " << x << " " << *(start-(x)+offset) << " " <<  *(start+(x+1)+offset) << "\n";
                cout << sizeFound << "\n";
                if(*(start-(x)+offset) != *(start+(x+1)+offset))
                    break;
                
                if(((x+1)*2) > sizeFound) {
                    longestFound = (char *)(start-x+offset);
                    sizeFound = ((x+1)*2);
                }
            }
            
            offset += 1;
            
        }
        
        longestFound[sizeFound]='\0';
        return std::string(longestFound);
    }
};