class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        
        def process(email):
            output = []
            inDomain = False
            isPlus = False
            for c in email:
                if isPlus: 
                    if c == "@":
                        inDomain = True
                        isPlus = False
                    else:
                        continue
                        
                elif c == "." and inDomain == False:
                    continue
                
                elif c == "+":
                    isPlus = True
                    continue
                    
                elif c == "@":
                    inDomain = True
                    
                output.append(c)
                
            return "".join(output)
        
        
        output = set()
        for email in emails:
            output.add(process(email))
            
        #print(output)
        return len(output)
                