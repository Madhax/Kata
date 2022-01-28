class TrieNode{
    
    public:
        char c;
        unordered_map<char,TrieNode*> mp;
        bool isWord;
        
        TrieNode(char c)
        {
            this->c=c;
            isWord=false;
        }
};

class WordDictionary {
public:
    
    TrieNode* root;
    
    WordDictionary() {
        root=new TrieNode(' ');
    }
    
    unordered_map<int,vector<string> > mp1;
    
    void addWord(string word) {
        mp1[word.length()].push_back(word);
    }
    
    bool search(string word) {
        int n=word.length();
        for(auto& s:mp1[n]){
                int i=0;
                while((i<n)&&(s[i]==word[i] || word[i]=='.')){
                    i++;
                }
                if(i==n)
                    return true;
            }
        return false;
        
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */