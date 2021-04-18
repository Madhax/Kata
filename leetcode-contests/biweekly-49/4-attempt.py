class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        originalBatchSize = batchSize
        groups = list(map(lambda x : x % batchSize, groups))
        
        happy = groups.count(0)
        groups = [x for x in groups if x != 0]
        
        groups.sort(reverse=True)
        total = sum(groups)
        print(groups, happy)
        
        #ctr = Counter(groups)
        
        def subset_sum(numbers, target, partial=[], partial_sum=0):
            if partial_sum == target:
                yield partial
            if partial_sum >= target:
                return
            for i, n in enumerate(numbers):
                remaining = numbers[i + 1:]
                yield from subset_sum(remaining, target, partial + [n], partial_sum + n)
                
                
        while True:
            try:
                pair = next(subset_sum(groups, batchSize))
            except:
                if batchSize < total:
                    batchSize += originalBatchSize 
                    continue
                else:
                    break
            print(pair)
            if pair is not None:
                for item in pair:
                    groups.remove(item)
                    total -= item
                happy += 1
            else:
                break

        print(groups)
        print(len(groups))
        return happy + (1 if len(groups) > 0 else 0)