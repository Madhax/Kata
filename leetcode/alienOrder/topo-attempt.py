# {a: [b, c]} means a is before b and c
def build_graph(words):
    g = {c: [] for w in words for c in w}
    for i in range(1, len(words)):
        for c1, c2 in zip(words[i-1], words[i]):
            if c1 != c2:
                g[c1].append(c2)
                break
    return g

def find_first_letter(g):
    s = set()
    for l in g.values():
        for c in l:
            s.add(c)
    first_letter = [c for c in g if c not in s]
    return first_letter

def explore(g, c, visited, result):
    if visited[c] == 1:
        raise Exception("cycle")
    if visited[c] == 2:
        return
    visited[c] = 1
    for c2 in g[c]:
        explore(g, c2, visited, result)
    result.append(c)
    visited[c] = 2

def topo_sort(g):
    visited = collections.defaultdict(lambda: 0)
    result = []
    letter = find_first_letter(g)[0]
    #for letter in find_first_letter(g):
    explore(g, letter, visited, result)

    result.reverse()
    return "".join(result)


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        return topo_sort(build_graph(words))
                    
        