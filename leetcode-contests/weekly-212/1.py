class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxLength = 0
        maxKey = None
        prevTime = 0
        for key, time in zip(keysPressed, releaseTimes):
            #print(key, time)
            releaseTime = time - prevTime
            prevTime = time
            if maxLength < releaseTime:
                maxKey = key
                maxLength = releaseTime
            if maxLength == releaseTime:
                if key > maxKey:
                    maxKey = key
       
        return maxKey
