import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return {k:s.count(k) for k in set(s)} == {
            k:t.count(k) for k in set(t)}
        