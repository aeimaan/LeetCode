class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        fmap = {}
        start = ord('a')
        for c in key:
            if c not in {' ', ',',':'} and c not in fmap:
                fmap[c] = start
                start += 1
        res = ""
        for i in range(len(message)):
            if message[i] in {' ', ',',':'}:
                res += message[i]
                continue
            res += chr(fmap[message[i]])
        return res
        