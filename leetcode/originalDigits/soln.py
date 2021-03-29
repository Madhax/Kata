class Solution:
    def originalDigits(self, s: str) -> str:
        #zero one two three four five six seven eight nine
        
        d = Counter(list(s))
        output = []
        if d["z"] > 0:
            mult = d["z"]
            output.extend(["0" * mult])
            d["z"] -= mult
            d["e"] -= mult
            d["r"] -= mult
            d["o"] -= mult
            
        if d["w"] > 0:
            mult = d["w"]
            output.extend(["2" * mult])
            d["t"] -= mult
            d["w"] -= mult
            d["o"] -= mult
            
        if d["u"] > 0:
            mult = d["u"]
            output.extend(["4" * mult])
            d["f"] -= mult
            d["o"] -= mult
            d["u"] -= mult
            d["r"] -= mult
            
        if d["x"] > 0:
            mult = d["x"]
            output.extend(["6" * mult])
            d["s"] -= mult
            d["i"] -= mult
            d["x"] -= mult
            
        if d["g"] > 0:
            mult = d["g"]
            output.extend(["8" * mult])
            d["e"] -= mult
            d["i"] -= mult
            d["g"] -= mult
            d["h"] -= mult
            d["t"] -= mult

        if d["o"] > 0:
            mult = d["o"]
            output.extend(["1" * mult])
            d["o"] -= mult
            d["n"] -= mult
            d["e"] -= mult
            
        if d["h"] > 0:
            mult = d["h"]
            output.extend(["3" * mult])
            d["t"] -= mult
            d["h"] -= mult
            d["r"] -= mult
            d["e"] -= mult
            d["e"] -= mult
            
        if d["f"] > 0:
            mult = d["f"]
            output.extend(["5" * mult])
            d["f"] -= mult
            d["i"] -= mult
            d["v"] -= mult
            d["e"] -= mult
            
        if d["v"] > 0:
            mult = d["v"]
            output.extend(["7" * mult])
            d["s"] -= mult
            d["e"] -= mult
            d["v"] -= mult
            d["e"] -= mult
            d["n"] -= mult

        if d["i"] > 0:
            mult = d["i"]
            output.extend(["9" * mult])
            d["n"] -= mult
            d["i"] -= mult
            d["n"] -= mult
            d["e"] -= mult
        
        return "".join(sorted(output))
        
        
        