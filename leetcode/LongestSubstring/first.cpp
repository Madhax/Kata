class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int charactersUsed[256];
        memset(charactersUsed, 0, sizeof(charactersUsed));
        unsigned int largestSubstring = 0;
        unsigned int substringSize = 0;
        unsigned int left = 0;
        unsigned int right = 0;
        unsigned int length = s.length();
        char rightChar;
        char leftChar;
        while(right < length)
        {
            rightChar = s[right];
            charactersUsed[rightChar]++;
            substringSize++;
            if(charactersUsed[rightChar] == 1) {
                if(substringSize > largestSubstring) {
                    largestSubstring = substringSize;
                }
            }
            while(charactersUsed[rightChar] == 2) {
                charactersUsed[s[left]]--;
                left++;
                substringSize--;
            }
            right++;
        }
        return largestSubstring;
    }
};