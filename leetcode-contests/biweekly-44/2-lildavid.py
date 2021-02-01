
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m=len(languages)
        Users=[set() for i in range(n+1)]
        for i in range(m):
            for x in languages[i]:
                Users[x].add(i+1)
        S=set()
        for x in friendships:
            suc=0
            for u in Users:
                if x[0] in u and x[1] in u:
                    suc=1
            if suc==0:
                S.add(x[0])
                S.add(x[1])
        return min([len([x for x in S if x not in Users[i]]) for i in range(1,n+1)])