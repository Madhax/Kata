class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       
        #()
        #(()), ()()
        #((())), ()(()), (()) (), (()())
        def buildList(n):
            output = set()
            output.add("()")
            while n > 1:
                newoutput = set()
                for item in output:
                    newoutput.add("()" + item)
                    newoutput.add(item + "()")
                    newoutput.add("(" + item + ")")
                    
                    x = 0
                    while x < len(item):
                        if item[x] == "(":
                            newitem = item[:x] + "()" + item[x:]
                            newoutput.add(newitem)
                            
                        if item[x] == ")":
                            newitem = item[:x] + "()" + item[x:]
                            newoutput.add(newitem)

                        x+=1
                        
                    #replace nth ()
                    
                output = newoutput
                n -= 1
            return output
       
       
        return buildList(n)