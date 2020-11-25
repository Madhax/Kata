class Solution:
    def calculate(self, s: str) -> int:
        
        def parse(s):
            commands = []
            lval = ""
            for x in s:
                if x.isdigit():
                    lval += x
                
                elif x == " ":
                    continue
                    
                else:
                    commands.append(int(lval))
                    lval = ""
                    commands.append(x)
            
            if lval != "":
                commands.append(int(lval))
            return commands
            
        def evaluate(commands):
            
            #evaluate *, /
            index = 0
            while index < len(commands):
                if commands[index] == "/":
                    val = floor(commands[index-1] / commands[index+1])
                    commands.insert(index-1, val)
                    del commands[index:index+3]
                elif commands[index] == "*":
                    val = floor(commands[index-1] * commands[index+1])
                    commands.insert(index-1, val)
                    del commands[index:index+3]
                else:
                    index += 1
                
            index = 0
            response = commands[0]
            while index < len(commands):

                if commands[index] == "+":
                    response += commands[index+1]
                    
                elif commands[index] == "-":
                    response -= commands[index+1]

                
                index += 1
                    
            return response
            
        
        return evaluate(parse(s))