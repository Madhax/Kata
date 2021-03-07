class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        

        incidence = Counter()
        seen = Counter()
        for edge in edges:
            etuple = (edge[0], edge[1])
            
            seen[etuple] += 1
            incidence[edge[0]] += 1
            incidence[edge[1]] += 1
            
        answers = Counter()
        
        newQueries = [(index, query) for (index, query) in enumerate(queries)]
        #print(newQueries)
        newQueries.sort(key=lambda x: x[1])
        #print(newQueries)
        
        for firstNode in range(1, n+1):
            for secondNode in range(firstNode+1, n+1):
                
                dampener = seen[(firstNode,secondNode)] + seen[(secondNode, firstNode)]
                numIncidence = incidence[firstNode] + incidence[secondNode] - dampener
                
                for query in newQueries:
                    if numIncidence > query[1]:
                        answers[query[0]] += 1
                    else:
                        break

        output = []
        for x in range(len(queries)):
            output.append(answers[x])
            
        return output
            