class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        U = len(pushed)
        O = len(popped)
       
        #simulate
       
        pushiter = 0
        popiter = 0
        stack = [-1]
       
        while pushiter < U and popiter < O:
           
            while pushiter < U and stack[-1] != popped[popiter]:
                stack.append(pushed[pushiter])
                pushiter += 1
               
           
            while popiter < O and stack[-1] == popped[popiter]:
                stack.pop()
                popiter += 1
               
        return pushiter == U and popiter == O and len(stack) == 1