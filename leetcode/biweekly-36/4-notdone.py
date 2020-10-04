class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = []
        serverLoad = []
        busyServers = []
        prevArrival = 1
        servers = [0]*k
        serverLoad = [0]*k
            
        for i in range(0, len(arrival)):
            time = arrival[i]
            timediff = time-prevArrival
            prevArrival=time
            for x in range(0, len(servers)):
                if servers[x] > 0:
                    servers[x] = max(servers[x]-timediff, 0)
                    if servers[x] == 0:
                        serverLoad[x] += 1
                        #busyServers.remove(server)
                        
                
            work = load[i]
            iter = i%k
            #print(iter)
            added = False
            while True:
                if servers[iter] == 0:
                    servers[iter] = work
                    added = True
                    break
                    
                iter += 1
                if iter >= k:
                    iter = 0
                if iter == i%k:
                    break   
            
            if added == False:
                print (busyServers, time, work, serverLoad, servers, i%k, (i%k)-1)
                    
            print(serverLoad, servers)
          
        #print(serverLoad, servers)
        maxLoad = 0            
        for x in range(0, len(servers)):
            if servers[x] > 0:
                servers[x] = 0
                serverLoad[x]+=1
            if serverLoad[x] > maxLoad:
                maxLoad = serverLoad[x]
                
        output = []
        for x in range(0, len(servers)):
            if serverLoad[x] == maxLoad:
                output.append(x)
        
        
            
        return output