<<<<<<< HEAD
import itertools

TICKS = 360 * 12 * 10**10

"""

"""

def solve(A,B,C):
    
    for V in itertools.permutations([A,B,C]):
        
        diff = V[1]-V[0]
        
        if diff < 0:
            print(diff)
            diff += TICKS
            print(diff)
            
        for rep in range(12):
            
            #diff == 11*x
            
            tmp = rep * TICKS + diff
            if tmp % 11 == 0:
                
                x = tmp // 11
                shift = V[0] - x

                if shift < 0:
                    shift += TICKS
                
                if (x + shift) % TICKS == V[0] and (12 * x + shift) % TICKS == V[1] and (720 * x + shift) % TICKS == V[2]:
                    print(rep, x, shift)
                    N = x % 1000000000
                    x //= 1000000000
                    
                    S = x % 60
                    x //= 60
                    M = x % 60
                    x //= 60
                    H = x
                    
                    return f"{H} {M} {S} {N}"

if __name__ == "__main__":
     t = int(input())
     for test in range(1, t+1):
         A, B, C = list(map(int, input().split()))
         
         print(f"Case #{test}: {solve(A,B,C)}")
=======
import math

totalTicks = 43200000000000
ticksPerHour = totalTicks/12
ticksHourToMinute = totalTicks/(12*60)
ticksHourToSecond = totalTicks/(12*60*60)

ticksPerMinute = totalTicks/60
ticksMinuteToSeconds = ticksPerMinute/60

ticksPerSecond = totalTicks/60

differentials = [0, totalTicks/8, totalTicks/4, totalTicks/2]
ticksPerDegree = totalTicks/360

def solve(angles):
    #choose one for hours
    #choose one for minutes
    #choose one for seconds

    #what is the invariant?
    chosen = set()
    for c in range(360):
        offset = c
        for h, a in enumerate(angles):
            chosen = set()
            (hours, leftoverHours) = divmod(a-(c*ticksPerDegree), ticksPerHour)

            if hours >= 12:
                continue
            
            chosen.add(h)

            for m, a2 in enumerate(angles):
                if m in chosen:
                    continue
            
                (minutes, leftoverMinutes) = divmod(a2-(c*ticksPerDegree), ticksPerMinute)
                
                if divmod(leftoverHours, ticksHourToMinute)[0] != minutes:
                    continue

                if minutes >= 60:
                    continue

                chosen.add(m)

                for s, a3 in enumerate(angles):
                    if s in chosen:
                        continue

                    (seconds, leftoverSeconds) = divmod(a3-(c*ticksPerDegree), ticksPerSecond)
                    
                    if seconds >= 60:
                        continue

                    if divmod(leftoverMinutes, ticksMinuteToSeconds)[0] != seconds:
                        continue

                    if leftoverSeconds > 0:
                        continue

                    #success
                    return "%d %d %d %d" % (hours, minutes, seconds, leftoverSeconds)
                    #return (hours, minutes, seconds, leftoverSeconds)


                chosen.remove(m)
            
            chosen.remove(h)

    return "0 0 0 0"
    #return ops
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        angles = list(map(int, input().split()))
        print(f"Case #{test}: {solve(angles)}")
>>>>>>> 10e847c23284beac0e5647c1a49906beaed6dc1b
