class Solution:
    def simplifyPath(self, path: str) -> str:
        while "//" in path or "/./" in path:
            path = path.replace("//", "/")
            path = path.replace("/./", "/")
           
        entities = path.split("/")
       
        iter = 0
        while iter < len(entities):
           
            if entities[iter] == "..":
                if iter > 0:
                    entities.pop(iter-1)
                    entities.pop(iter-1)
                    iter -= 1
                else:
                    entities.pop(iter)
            elif entities[iter] == ".":
                entities.pop(iter)  
            else:
                iter += 1
           
        output = "/".join(entities)
           
        if output == "":
            output = "/"
       
        if output[0] != "/":
            output = "/" + output
       
        if len(output) > 1 and output[-1] == "/":
            return output[:-1]
       
        return output
