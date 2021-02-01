class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        toTeach = set()
        for u, v in friendships:
            if len(set(languages[u-1]).intersection(languages[v-1])) == 0:
                toTeach.add(u-1)
                toTeach.add(v-1)
        l = [0] * n
        for i in toTeach:
            for la in languages[i]:
                l[la-1] += 1
        return len(toTeach) - max(l)
            