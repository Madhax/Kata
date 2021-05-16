class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(val):
            
            if len(val) == 0:
                return False
            
            if val[0] == "+" or val[0] == "-":
                start = 1
                if len(val) == 1:
                    return False
            else:
                start = 0
                
            
            return all([x.isdigit() for x in val[start:]])
        
        def isDecimal(val):
            if len(val) == 0:
                return False
            if "." not in val:
                return False
            
            if val[0] == "+" or val[0] == "-":
                start = 1
            else:
                start = 0
                
            components = val[start:].split(".")
            if len(components) > 2:
                return False
            if components[0] == "" and components[1] == "":
                return False
            
            return (components[0].isdigit() or len(components[0]) == 0) and  (components[1].isdigit() or len(components[1]) == 0)
        
            
        if "e" in s:
            components = s.split("e")
            if len(components) > 2:
                return False
            return (isDecimal(components[0]) or isInteger(components[0])) and isInteger(components[1])
        elif "E" in s:
            components = s.split("E")
            if len(components) > 2:
                return False
            return (isDecimal(components[0]) or isInteger(components[0])) and isInteger(components[1])
        else:
            return isDecimal(s) or isInteger(s)
            
        #print(isInteger("+123"))
        return 0