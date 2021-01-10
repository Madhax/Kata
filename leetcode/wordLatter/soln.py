from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        def isOneOff(word1, word2):
            numDiffs = 0
            for x in range(len(word1)):
                if word1[x] != word2[x]:
                    numDiffs += 1
                    if numDiffs >= 2:
                        return False
            return True
        
        
        def bfs(word, goal):
            nonlocal wordList
            visited = set()
            visited.add(word)
            q = deque()
            newSet = set()
            for newWord in wordList:
                if isOneOff(word, newWord):
                    if newWord == goal:
                        return 2
                    else:
                        q.append([newWord, 2])
                        newSet.add(newWord)
            
            wordList -= newSet
                        
            while len(q):
                [currentWord, work] = q.popleft()
                if currentWord in visited:
                    continue
                visited.add(currentWord)
                newSet = set()
                for newWord in wordList:
                    if newWord not in visited and isOneOff(currentWord, newWord):
                        if newWord == goal:
                            return work+1
                        else:
                            q.append([newWord, work+1])
                            newSet.add(newWord)
                            
                wordList -= newSet
            return 0
        
        return bfs(beginWord, endWord)
                        