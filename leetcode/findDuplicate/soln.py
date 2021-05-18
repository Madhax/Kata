class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(set)
        
        for path in paths:
            components = path.split(" ")
            
            for file in components[1:]:
                fileParts = file.split("(")
                fileContents = fileParts[1][:-1]
                d[fileContents].add(str(components[0] + "/" + fileParts[0]))
        
        output = []
        
        for item in d.values():
            if len(item) > 1:
                output.append(list(item))
                
        return output