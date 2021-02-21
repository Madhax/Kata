from collections import deque
#from bisect import *

class PlaylistQueue:
    def __init__(self, songs):
        #print(len(songs))
        self.s = deque(songs)

    def play(self, i):
        song = self.delete_nth(self.s, i)
        self.s.append(song)
        return song

    def delete_nth(self, d, n):
        d.rotate(-n)
        ret = d.popleft()
        d.rotate(n)
        return ret