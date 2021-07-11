class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        '**' >> 96
        
        11 12 13 14 ...19
        21 22 23       29
        .
        .
        .
        91 92 93  .....99

        10 11 ...26


        Then 89 + 17 = 96
        '''
        mod = 10**9 + 7
        a, b, c = 1, 0, 0 
        for ch in s:
            if not a and not b and not c:
                return 0
            if ch == '*':
                a, b, c = a*9+b*9+c*6, a, a
            else:
                a, b, c = (ch > '0') * a + b + (ch<='6')*c , (ch == '1') * a, (ch=='2')*a
            
            a %= mod
            
        return a