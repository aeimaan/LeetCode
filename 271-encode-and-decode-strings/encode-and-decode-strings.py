class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += f"{len(s):06d}"
            res += s
        return res


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            length = int(s[i:i+6])
            decoded_str = s[i+6:i+6+length]
            res.append(decoded_str)
            i +=  length + 6
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))