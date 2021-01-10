class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        valueIndices = {}
        
        def hDistance(seq1, seq2):
            ret = 0
            for x in range(len(seq1)):
                if seq1[x] != seq2[x]:
                    ret += 1
                    
                if seq1[x] not in valueIndices:
                    valueIndices[seq1[x]] = [x]
                    
                else:
                    valueIndices[seq1[x]].append(x)
                
            return ret
        
        transitions = {}
        
        
        added = True
        while added:
            added = False

            for [i,j] in allowedSwaps:
                if i not in transitions:
                    transitions[i] = set([j])
                    added = True

                if j not in transitions:
                    transitions[j] = set([i])
                    added = True
                    
                transitions[i].add(j)
                transitions[j].add(i)
                if transitions[j] != transitions[i]:
                    transitions[j] = transitions[j].union(transitions[i])
                    transitions[i] = transitions[i].union(transitions[j])
                    added = True
                
        print(transitions)
        hammingDistance = hDistance(source, target)
        
        #print(hammingDistance)
        tookFrom = set()
        
        for x in range(len(source)):
            if source[x] != target[x] and target[x] in valueIndices:
                #bestTake = [float("-inf"), 0,0]
                for index in valueIndices[target[x]]:
                    if x in transitions and index in transitions[x] and index not in tookFrom and x not in tookFrom:
                        if x == index:
                            continue
                        #print(x, index, target[x], source[index])
                        hammingDistance-=1
                        tookFrom.add(index)
                        tookFrom.add(x)
                        #if target[x] == source[x]:
                            #print("here")
                        #    hammingDistance-=1
                         #   tookFrom.add(x)
                        
                        #if take > bestTake[0]:
                        #    bestTake=[take, index, x]
                        break
                """if bestTake[0] > 0:
                    hammingDistance -= bestTake[0]
                    tookFrom.add(bestTake[1])
                    if bestTake[0] == 2:
                        tookFrom.add(bestTake[2])"""
        
                    
        return hammingDistance