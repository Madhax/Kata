class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        exact = set()
        caseInsensitive = defaultdict(list)
        vowelInsensitive = defaultdict(list)
        
        for word in wordlist:
            exact.add(word)
            caseInsensitive[word.lower()].append(word)
            vowelInsensitive[word.lower().replace("e", "a").replace("i", "a").replace("o", "a").replace("u", "a")].append(word)
            
        output = []
        #print(caseInsensitive, vowelInsensitive)
        for query in queries:
            ql = query.lower()
            qi = query.lower().replace("e", "a").replace("i", "a").replace("o", "a").replace("u", "a")
            if query in exact:
                output.append(query)
            elif ql in caseInsensitive:
                output.append(caseInsensitive[ql][0])
            elif qi in vowelInsensitive:
                output.append(vowelInsensitive[qi][0])
            else:
                output.append("")
        
        return output
        