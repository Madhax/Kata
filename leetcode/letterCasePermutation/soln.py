class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
       
        output = []
        def permute(index, cand):
            nonlocal output
            #print(index, cand)
            if index == len(cand):
                output.append("".join(cand))
                return
       
            if cand[index].isalpha():
                cand[index] = cand[index].upper()
               
                permute(index+1, cand)
               
                cand[index] = cand[index].lower()
               
                permute(index+1, cand)
               
            else:
                permute(index+1, cand)
            return
           
        permute(0, list(S))
        return output
