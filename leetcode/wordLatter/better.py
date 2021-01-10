class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # corner case
        if endWord not in wordList:
            return 0
        
        # init front and back set to search
        front = {beginWord}
        back = {endWord}
        
        # increase search speed to O(1)
        wordList = set(wordList)
        trans = 1
        len_word = len(beginWord)
        
        # BFS starts here
        while front:
            trans += 1
            next_front = set()
            
            for word in front:
                for i in range(len_word):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        
                        if new_word in back:
                            return trans
                        
                        if new_word in wordList:
                            next_front.add(new_word)
                            wordList.remove(new_word)
                            
            front = next_front
            
            if len(back) < len(front):
                front, back = back, front
                
        # corner case
        return 0