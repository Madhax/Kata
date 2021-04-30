# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        # keep track of candidates
        candidates = {word: 0 for word in wordlist}
        
        # update scores of words related to our guess
        def update_score(word, guess, guess_score):
            for i in range(len(word)):
                if word[i] == guess[i]:
                    if guess_score == 0:
                        del candidates[word]
                        return
                    candidates[word] += 1
        
        # search for candidate with the highest score
        attempts = 0
        while len(candidates) > 0 and attempts < 10:
            _, guess = min([(-score, word) for word, score in candidates.items()])
            guess_score = master.guess(guess)
            if guess_score == len(guess):
                return
            del candidates[guess]
            for candidate in list(candidates.keys()):
                update_score(candidate, guess, guess_score)
            attempts += 1