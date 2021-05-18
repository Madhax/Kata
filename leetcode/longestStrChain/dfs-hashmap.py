class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def get_predecessors(node):
            res = []
            n = len(node)
            for i in range(n):
                word = node[:i] + node[i+1:]
                if word in length_hashmap[n-1]:
                    res.append(word)
            return res
            
        def dfs(node):
            visited.add(node)
            count = 0
            for predecessor in get_predecessors(node):
                # we don't need to check visited set here, based on the problem definition
                # we will not revisit a node if we trace the words chain backward.
                if predecessor not in visited:
                    count = max(count, dfs(predecessor))
            return count + 1
            
        # build length_hashmap to save neighbor lookup time
        length_hashmap = collections.defaultdict(set)
        for word in words:
            length_hashmap[len(word)].add(word)    
        
        visited = set()
        longest = 0
        min_length = min(length_hashmap)
        # start from the longest words
        for length in sorted(length_hashmap, reverse=True):
            for word in length_hashmap[length]:
                # skipping checking captured/visited nodes 
                if word in visited:
                    continue
                longest = max(longest, dfs(word))
                # no enough words to break the record
                if length - min_length < longest:
                    return longest
        return longest