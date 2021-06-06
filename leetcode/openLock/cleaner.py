class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        front, back = set(['0000']), set([target])
        level = 1
        
        while front:
            new_front = set()
            for item in front:
                for i in range(len(item)):
                    for j in [(int(item[i]) + 1) % 10, (10 + int(item[i]) - 1) % 10]:
                        new_item = item[:i] + str(j) + item[i + 1:]
                        if new_item in back:
                            return level
                        if new_item in deadends:
                            continue
                        new_front.add(new_item)
                        deadends.add(new_item)
            if len(new_front) > len(back):
                new_front, back = back, new_front
            front = new_front
            level += 1
        
        return -1