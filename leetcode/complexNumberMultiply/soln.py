class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        com1 = num1.split("+")
        com1[1] = com1[1][:-1]
        com2 = num2.split("+")
        com2[1] = com2[1][:-1]
        
        #print(com1, com2)
        part1 = int(com1[0]) * int(com2[0])
        #print(part1)
        part1 += (int(com1[1]) * int(com2[1]) * (-1))
        #print((int(com2[0]) * int(com2[0]) ))
        part2 = int(com1[0]) * int(com2[1])
        part2 += int(com1[1]) * int(com2[0])
        
        #print(part1, part2)
        
        return "{}+{}i".format(str(part1), str(part2))