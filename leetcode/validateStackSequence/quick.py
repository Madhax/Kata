class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        num_popped = 0
        for n in pushed:
            st.append(n)
            while st and st[-1] == popped[num_popped]:
                st.pop()
                num_popped += 1
        return not st and num_popped == len(popped)        
        