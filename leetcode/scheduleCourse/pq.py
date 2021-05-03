import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        O(nlog(n)) time, O(n) space. Refer to last approach in solution tab.
        """
        sorted_courses = sorted(courses, key=lambda course: course[1])
    
        pq = [] # Max-heap so push negatives
        
        time = 0
        for course in sorted_courses:
            # If course can finish before its last possible day, add to pq
            if time + course[0] <= course[1]:
                heapq.heappush(pq, -course[0])
                time += course[0]
            # If course cannot finish before last possible day but its duration is less than
            # duration of longest course in heap, remove longest course on heap and add new course since 
            # new course end time definitely sufficient (smaller duration and courses were sorted by end time)
            elif pq and -pq[0] > course[0]:
                # recalculate time (remove duration of heap top a and add duration of new course)
                time += course[0] - -heapq.heappop(pq)
                heapq.heappush(pq, -course[0])
        
        return len(pq)