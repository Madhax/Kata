class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # 10110
        # 10011
        # 11011

        if "0" not in binary:
            return binary
        
        N = len(binary)
        index = binary.index("0")
        
        ans = []
        for y in range(index):
            ans.append(binary[y])
            
        zeroes = 0
        ones = 0
        for y in range(index, N):
            if binary[y] == "0":
                zeroes += 1
            else:
                ones += 1
                
        #print(zeroes, ones)
        while zeroes >= 2:
            zeroes -= 1
            ans.append("1")
            
        ans.append("0")
        while ones >= 1:
            ones -= 1
            ans.append("1")

        return "".join(ans)
