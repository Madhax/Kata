class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        def transform(word):
            nonlocal morseCodes
            return "".join([morseCodes[ord(x) - ord('a')] for x in word])
        
        transformations = set()
        for word in words:
            transformations.add(transform(word))
            
        return len(transformations)