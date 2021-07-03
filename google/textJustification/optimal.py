class Solution:
    def formatLine(self, lst, maxWidth, lastLine):
        totlen = sum([len(x) for x in lst])
        spaces = maxWidth - totlen
        places = len(lst) - 1
        if places == 0:
            return lst[0] + " "*spaces
        else:
            if lastLine:
                extraspaces =  spaces - places
                return " ".join(lst) + " "*extraspaces
            else:
                spaceperplace = int(spaces/places)
                leftover = mod(spaces, places)
                spaceList = [" "*(spaceperplace + 1)] * leftover + [" "*spaceperplace] * (places - leftover)
                w = lst[0]
                for i in range(places):
                    w = w + spaceList[i]
                    w = w + lst[i+1]
                return w
            
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        alllines = []
        line = []
        len1 = 0
        for word in words:
            if len1 ==0:
                len1 += len(word)
            else:
                len1 += 1
                len1 += len(word)
            if len1 <= maxWidth:
                line.append(word)
            else:
                alllines.append(self.formatLine(line, maxWidth, False))
                line = []
                len1 = len(word)
                line.append(word)
        alllines.append(self.formatLine(line, maxWidth, True))
        #print(alllines)
        return alllines