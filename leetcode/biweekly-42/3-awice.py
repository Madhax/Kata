class Solution(object):
    def maximumBinaryString(self, S):
        A = deque()
        done = 0
        for c in S:
            if c == '0':
                if A and A[0] == '0':
                    done += 1
                else:
                    A.append(c)
            else:
                if not A:
                    done += 1
                else:
                    A.append(c)
            # print("!", A, done)
        
        return '1' * done + "".join(A)