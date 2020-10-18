import string
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        intrans = "ACGT"
        outtrans = "0123"
        trantab = str.maketrans(intrans, outtrans)
        sLen = len(s)
        end = 10
        start = 0
        output = set()
        d = {}
        while end <= sLen:
            substr = s[start:end]
            #print(substr)
            val = int(substr.translate(trantab))
            if val in d:
                output.add(substr)
            else:
                d[val] = True
            start += 1
            end += 1
            
        return output