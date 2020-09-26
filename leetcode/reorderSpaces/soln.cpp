class Solution {
public:
    string reorderSpaces(string text) {
        int spaces = count(text.begin(), text.end(), ' ');
        vector<string> words;
        string output = "";
        string s = text;
        int pos;
        while ((pos = s.find(' ')) != std::string::npos) {
            string token = s.substr(0, pos);
            //std::cout << token << std::endl;
            if(token.size() > 0) {
                words.push_back(token);
                //cout << token << "\n";
            }
            s.erase(0, pos + 1);
        }
        if(s.size() > 0) {
            //cout << s << "\n";
            words.push_back(s);
        }
        //(words.size() == 0) words.push_back(text);
        int innerSpaces, trailingSpaces;
        cout << words.size() << "\n";
        if(words.size()-1 == 0) {
            innerSpaces = 0;
            trailingSpaces = spaces;
        }
        else {
            innerSpaces = (int) floor(spaces/(words.size()-1));
            if(innerSpaces == 1) {
                trailingSpaces = spaces % (words.size()-1);
            }
            else {
                trailingSpaces = spaces % innerSpaces;
            }
            
        }
        //cout << innerSpaces << " " << trailingSpaces << " " << (words.size()-1) << " " << spaces << "\n";
        for(auto iter = words.begin(); iter != words.end(); iter++) {
            //cout << *iter << "\n";
            output += *iter;
            if(iter != words.end() -1) {
                for(int x = 0; x < innerSpaces; x++) {
                    output += " ";
                }
            }
        }
        for(int x = 0; x < trailingSpaces; x++) {
            output += " ";
        }
        
        return output;
    }
};