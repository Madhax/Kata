class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        work = []
        for idx, state in enumerate(dominoes):
            if state == "L":
                if idx > 0 and dominoes[idx-1] == ".":
                    work.append((state, idx))
                    
            elif state == "R":
                if idx < len(dominoes)-1 and dominoes[idx+1] == ".":
                    work.append((state, idx))
                    
        dominoes=list(dominoes)
        workToDo = True
        while workToDo:
            workToDo = False
            #pendingChanges = defaultdict(str)
            pendingChanges = []
            #newDominoes = dominoes[:]
            while work:
                workToDo = True
                state, idx = work.pop()
                #print(state, idx)
                if state == "L":
                    if idx > 0:
                        if idx - 1 > 0 and dominoes[idx-1] == "." and dominoes[idx-2] == "R":
                            continue
                                
                        elif dominoes[idx-1] == ".":
                            pendingChanges.append((idx-1, "L"))
                            #dominoes[idx-1] = "L"
                    
                if state == "R":
                    if idx < len(dominoes)-1:
                        if idx < len(dominoes)-2 and dominoes[idx+1] == "." and dominoes[idx+2] == "L":
                            continue
                        elif dominoes[idx+1] == ".":
                            pendingChanges.append((idx+1, "R"))
                            #dominoes[idx+1] = "R"
            #print("HERE", pendingChanges)
            for idx, change in pendingChanges:
                #print(idx, change)
                dominoes[idx] = change
                work.append((change, idx))
                
        return "".join(dominoes)
                
                                                  
                    
                    
                    
            