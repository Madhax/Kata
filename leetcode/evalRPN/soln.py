class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        s = []
        result = None
        
        for symbol in tokens:
            try:
                val = int(symbol)
                is_dig = True
            except:
                is_dig = False
                
            if is_dig:
                s.append(val)
            else:
                rval = s.pop()
                lval = s.pop()
                #print(lval, symbol, rval)
                if symbol == "+":
                    lval += rval
                elif symbol == "-":
                    lval -= rval
                elif symbol == "*":
                    lval *= rval
                elif symbol == "/":
                    lval = int(lval / rval)
                s.append(lval)
                
                #print(symbol, lval)
        result = s.pop()
        return result
                
            