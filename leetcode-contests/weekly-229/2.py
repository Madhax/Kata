class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        balls = []
        boxes = list(boxes)
        for index, box in enumerate(boxes):
            if box == "1":
                balls.append(index)
                
        output = []
        
        for index, box in enumerate(boxes):
            diff = 0
            for item in balls:
                diff += abs(index-item)
            output.append(diff)
        
        return output