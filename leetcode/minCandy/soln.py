class Solution:
    def candy(self, ratings: List[int]) -> int:
        q = []
        if len(ratings) == 1:
            return 1
        
        for idx, rating in enumerate(ratings):
            heappush(q, (rating, idx))
            
        work = [0 for _ in range(len(ratings))]
        candies = 0
        while q:
            rating, idx = heappop(q)
            #print(rating, idx)
            if idx == 0:
                if work[idx+1] > 0:
                    if ratings[idx+1] < ratings[idx]:
                        work[idx] = work[idx+1] + 1
                    else:
                        work[idx] = 1
                    
                else:
                    work[idx] = 1
                    
            elif idx == len(ratings)-1:
                if work[idx-1] > 0:
                    if ratings[idx-1] < ratings[idx]:
                        work[idx] = work[idx-1] + 1
                    else:
                        work[idx] = 1
                    
                else:
                    work[idx] = 1
                    
            else:
                maxRating = math.inf
                maxCandy = 0
                if work[idx-1] > 0:
                    if ratings[idx-1] < ratings[idx]:
                        maxRating = min(maxRating, ratings[idx-1])
                        maxCandy = max(maxCandy, work[idx-1])
                
                if work[idx+1] > 0:
                    if ratings[idx+1] < ratings[idx]:
                        maxRating = min(maxRating, ratings[idx+1])
                        maxCandy = max(maxCandy, work[idx+1])

                if maxRating < ratings[idx]:
                    work[idx] = maxCandy+1
                    
                elif maxCandy > 0:
                    work[idx] = 1
                    
                else:
                    work[idx] = 1
                
            candies += work[idx]
            
        #print(work)
        return candies
            