class Codec:

    d = defaultdict(str)
    pk = 0
   
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.d[self.pk] = longUrl
        return str(self.pk)
       

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[int(shortUrl)]
   

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url)) 