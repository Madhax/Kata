class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        graph = defaultdict(set)
        
        def diffByOne(word1, word2):
            numDiff = 0
            for x in range(len(word1)):
                if word1[x] != word2[x]:
                    numDiff += 1
                    
            return numDiff == 1
        
        wordList.append(beginWord)
        for x in range(len(wordList)):
            for y in range(x+1, len(wordList)):
                if diffByOne(wordList[x], wordList[y]):
                    #print(wordList[x], wordList[y])
                    graph[wordList[x]].add(wordList[y])
                    graph[wordList[y]].add(wordList[x])
                
        if endWord not in graph:
            return None
        
        
        def bfs(startNode):
            
            q = deque()
            
            q.append((startNode, 1, set))
            
            output = []
            while q:
                
                curNode,  
                
                
            return output
            
        """
        seen=set()
        curStack = []
        output = []
        curBest = math.inf
        def dfs(word):
            nonlocal curBest, output, curStack, seen
            if len(curStack) > curBest:
                return 
            if word == endWord and len(curStack) <= curBest:
                if len(curStack) == curBest:
                    output.append(curStack.copy())
                else:
                    output = []
                    output.append(curStack.copy())
                    curBest = len(curStack)
                    
                return
                
            for newWord in graph[word]:
                if newWord not in seen:
                    seen.add(newWord)
                    curStack.append(newWord)
                    dfs(newWord)
                    curStack.pop()
                    seen.remove(newWord)
                    
        curStack.append(beginWord)
        seen.add(beginWord)
        """
        
        bfs
        
        dfs(beginWord)
        return output
        
                