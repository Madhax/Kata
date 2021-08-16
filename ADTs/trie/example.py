from functools import reduce
from collections import defaultdict
T = lambda : defaultdict(T)
trie = T()
reduce(dict.__getitem__,'how',trie)['isEnd'] = True

#search
curr = trie
for w in 'how':
    if w in curr:
        curr = curr[w]
    else:
        print("Not Found")
        break
if curr['isEnd']:
    print('Found')


##OR

from collections import defaultdict
_trie = lambda: defaultdict(_trie)
#create
trie = _trie()
for s in ["cat", "bat", "rat", "cam"]:
    curr = trie
    for c in s:
        curr = curr[c]
    curr.setdefault("_end")
#lookup
def word_exist(trie, word):
    curr = trie
    for w in word:
        if w not in curr:
            return False
        curr = curr[w]
    return '_end' in curr