struct TrieNode {
    TrieNode* charSet[26];
    bool end;
};

class WordDictionary {
    TrieNode* root = new TrieNode();
    
    bool doesExist(TrieNode* node, string word, int index) {
        if (index==word.size()) {
            return node->end;
        }
        if (word[index] == '.') {
            bool ret = false;
            for (auto& it: node->charSet) {
                if(it) {
                    ret = doesExist(it, word, index+1);
                    if (ret) {
                        return true;
                    }
                }
            }
        }
        else {
            auto& child = node->charSet[word[index]-'a'];
            if (child) {
                return doesExist(child, word, index+1);
            }
        }
        return false;
    }
    
public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for (auto& c : word) {
            int i = c - 'a';
            if (node->charSet[i] == 0) {
                node->charSet[i] = new TrieNode();
            }
            node = node->charSet[i];
        }
        node->end = true;
    }
    
    bool search(string word) {
        return doesExist(root, word, 0);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */