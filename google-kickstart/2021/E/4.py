def solve(cards):
    
    return (1/cards) * ((cards)*(cards+1)/2)

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        
        cards = int(input())
        print(f"Case #{test}: {solve(cards)}")

"""
2
start
jjj
"""