class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'}
       
        output = []
       
        work = []
        def build(index):
            nonlocal output, work
            if len(work) == len(digits) and len(digits) > 0:
                #print(work, digits)
                output.append("".join(work))
            elif index < len(digits):
                for c in d[digits[index]]:
                    #print(c)
                    work.append(c)
                    build(index+1)
                    work.pop()
       
        build(0)
        return output

                