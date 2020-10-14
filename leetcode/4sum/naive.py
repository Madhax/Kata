class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        for x1 in range(0, len(nums)):
            for x2 in range(x1+1, len(nums)):
                if target < nums[x1] and nums[x2] > 0:
                    break    
                part1 = nums[x1] + nums[x2]
                for x3 in range(x2+1, len(nums)):
                    if target < part1 and nums[x3] > 0:
                        break
                    part2 = part1 + nums[x3]
                    for x4 in range(x3+1, len(nums)):
                        if target < part2 and nums[x3] > 0:
                            break
                        part3 = part2 + nums[x4]
                        if part3== target:
                            output.append([nums[x1],nums[x2],nums[x3],nums[x4]])
                            
        output=[ii for n,ii in enumerate(output) if ii not in output[:n]]

        return output