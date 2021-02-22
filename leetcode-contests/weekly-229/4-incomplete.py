class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        
        def lcs(S1, S2, m, n):
            L = [[0 for x in range(n+1)] for x in range(m+1)]

            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif S1[i-1] == S2[j-1]:
                        L[i][j] = L[i-1][j-1] + 1
                    else:
                        L[i][j] = max(L[i-1][j], L[i][j-1])

            index = L[m][n]

            lcs_algo = [""] * (index+1)
            lcs_algo[index] = ""

            i = m
            j = n
            while i > 0 and j > 0:

                if S1[i-1] == S2[j-1]:
                    lcs_algo[index-1] = S1[i-1]
                    i -= 1
                    j -= 1
                    index -= 1

                elif L[i-1][j] > L[i][j-1]:
                    i -= 1
                else:
                    j -= 1

            return "".join(lcs_algo)

        
        word1backup = word1
        word2backup = word2
        word1 = word1 + word2
        word2 = word2[::-1] + word1backup[::-1]
        m = len(word1)
        n = len(word2)
        
        lcs = lcs(word1, word2, m, n)
        
        
        
        
        print(lcs)
        output = len(lcs)
        
        if lcs[0] in word1backup and lcs[-1] in word2backup:
            return output
        else:
            return 0
        """
        output = len(lcs) * 2
        
        if output == 0:
            return 0
        
        #check for floating 
        
        index = 0
        iter = 0
        #print(output, lcs)
        while index < len(lcs) and iter < len(word1):
            if word1[iter] == lcs[index]:
                index += 1
                
                if index == len(lcs) and iter < len(word1) - 1:
                    return output +1
                elif index == len(lcs):
                    break
            iter += 1
            
        index = 0
        iter = 0
        
        while index < len(lcs) and iter < len(word2):
            #print(iter, index)
            if word2[iter] == lcs[index]:
                index += 1
                
                if index == len(lcs) and iter < len(word2) - 1:
                    return output +1
                elif index == len(lcs):
                    break
            iter += 1
        """
        return output