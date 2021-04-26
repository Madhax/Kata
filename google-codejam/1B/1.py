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