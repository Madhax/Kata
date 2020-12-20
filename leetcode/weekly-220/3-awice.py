class MMQueue:
    def __init__(self):
        self.maq = collections.deque()
        self.len = 0
    
    def enqueue(self, v):
        self.len += 1
        
        c = 1
        while self.maq and self.maq[-1][0] < v:
            c += self.maq.pop()[1]
        self.maq.append([v, c])
    
    def dequeue(self):
        self.len -= 1
        
        self.maq[0][1] -= 1
        if self.maq[0][1] <= 0:
            self.maq.popleft()
    
    def max(self):
        return self.maq[0][0] if self.maq else 0
    
    def __len__(self):
        return self.len
class Solution:
    def maxResult(self, A: List[int], K: int) -> int:
        N = len(A)
        mq = MMQueue()
        mq.enqueue(A[0])
        ans = A[0]
        for i in range(1, N):
            if len(mq) > K:
                mq.dequeue()
            ans = A[i] + mq.max()
            mq.enqueue(ans)
        return ans