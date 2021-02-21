class Solution:
    def solve(self, reviews, threshold):
        ctr = 0
        num = 0
        den = 0
        for i in range(len(reviews)):
            num += reviews[i][0]
            den += reviews[i][1]
            """
            while (reviews[i][0] / reviews[i][1]) < (threshold/100):
                print(i, reviews[i][0], reviews[i][1])
                ctr += 1
                reviews[i][0] += 1
                reviews[i][1] += 1
            """
        while num/den < (threshold/100):
            ctr += 1
            num += 1
            den += 1
            
        return ctr
