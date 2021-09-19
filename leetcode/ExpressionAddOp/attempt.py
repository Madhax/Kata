class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        output = set()
        work = []
        def buildOutput(index, usedOp):
            nonlocal work
            if index == len(num) :
                if usedOp and '0'<=work[-1]<='9':
                    try:
                        if eval("".join(work)) == target:
                            output.add("".join(work))
                    except:
                        pass
                return
            if len(work) == 0:
                work.append(num[index])
                buildOutput(index+1, usedOp)
                work.pop()
                
            elif '0' <= work[-1] <= '9':
                #can be digit, can be operator
                work.append("+")
                buildOutput(index, True)
                work.pop()
                
                work.append("-")
                buildOutput(index, True)
                work.pop()
                
                work.append("*")
                buildOutput(index, True)
                work.pop()
                
                if work[-1] != "0":
                    work.append(num[index])
                    buildOutput(index+1, usedOp)
                    work.pop()
            else:
                #must be digits
                work.append(num[index])
                buildOutput(index+1, usedOp)
                work.pop()
                
        buildOutput(0, False)
        return list(output)