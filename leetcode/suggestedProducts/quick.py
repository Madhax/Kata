class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Ugly Brute Force Solution takes 40min to figure out and debug
#         products.sort()
#         cp = products.copy()
#         ans = []
#         skip = set()
        
#         for i, ch in enumerate(searchWord):
#             tmp = []
#             j = 0
#             while j < len(cp):
#                 if j not in skip:
#                     if i >=  len(cp[j]):
#                         j += 1
#                         continue
#                     if cp[j][i] == ch and len(tmp) < 3:
#                         tmp.append(cp[j])
#                     if cp[j][i] != ch:
#                         skip.add(j)
#                 j += 1
#             ans.append(tmp)
#         return ans
        
        # Binary Search
        products.sort()
        ans = []
        prefix = ''
        for ch in searchWord:
            prefix += ch
            l = bisect.bisect_left(products, prefix)
            r = bisect.bisect_right(products, prefix + '~')
            if l == r: # no such word
                break 
            ans.append(products[ l : min(l+3, r) ])
        while len(ans) < len(searchWord): # append empty list when not found
            ans.append([])
        return ans