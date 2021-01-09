class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        output = ""
        while len(number) > 0:
            if len(output) > 0:
                output += "-"
            if len(number) > 4:
                output += number[:3]
                number = number[3:]
                
            elif len(number) == 4:
                output += number[:2] + "-" + number[2:4]
                number = number[4:]
                
            else:
                output += number
                number = ""
            
        return output