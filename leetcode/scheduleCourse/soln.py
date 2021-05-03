from sortedcontainers import SortedList
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        courses.sort(key=lambda x: x[1])
        
        @functools.cache
        def dp(index, currentDay):
            #print(index, currentDay)
            if index == len(courses):
                return 0
            best = 0
            
            #print(currentDay + courses[index][0], currentDay + courses[index][1])
            if (currentDay + courses[index][0]) <= (courses[index][1]):
                best = max(best, 1+dp(index+1, currentDay + courses[index][0]))
                
            #skip
            best = max(best, dp(index+1, currentDay))
            return best
            
        return dp(0, 0)
        """
        courses.sort(key=lambda x: x[1])
        #print(courses)
        sl = SortedList()
        currentTotalTime = 0
        courseCount = 0
        for duration, lastDay in courses:
            
            if duration + currentTotalTime <= lastDay:
                currentTotalTime += duration
                sl.add((duration))
                courseCount += 1
            else:
                if len(sl) > 0 and sl[-1] > duration and (currentTotalTime-sl[-1] + duration) <= lastDay:
                    val = sl[-1]
                    currentTotalTime -= val
                    currentTotalTime += duration
                    sl.remove(val)
                    sl.add(duration)
                    #courseCount += 1
            #print(currentTotalTime, duration, lastDay, courseCount, sl)
        return courseCount
            