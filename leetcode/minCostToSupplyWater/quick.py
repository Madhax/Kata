
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        unions = list(range(n+1)); unions[0] = -1
        def find(i): # with zipping
            if unions[i] != i: unions[i] = find(unions[i])
            return unions[i]
        
        total = sum(wells)
        destroyed = set()
        for i, j, cost in sorted(pipes, key=lambda pipe: pipe[2]):
            dst, rsv = find(i), find(j)
            if dst == rsv: continue
            if dst in destroyed or (wells[dst-1] < wells[rsv-1] and rsv not in destroyed):
                dst, rsv = rsv, dst # not destroyed and max cost
            if dst in destroyed: continue
            
            if wells[dst-1] > cost: # build a pipe and destory well
                total += cost - wells[dst-1]
                destroyed.add(dst)
                unions[dst] = rsv # update destroyed's root as reserved
        return total