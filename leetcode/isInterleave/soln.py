class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        @functools.cache
        def dp(s1i, s2i, s3i):
            valid = False

            if s3i == len(s3):
                return True

            if s1i < len(s1):
                if s1[s1i] == s3[s3i]:
                    valid |= dp(s1i+1, s2i, s3i+1)
                    if valid:
                        return True

            if s2i < len(s2):
                if s2[s2i] == s3[s3i]:
                    valid |= dp(s1i, s2i+1, s3i+1)
                    if valid:
                        return True

            return valid


        return dp(0, 0, 0)