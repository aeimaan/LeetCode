class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        fmap = {}
        res = []

        for word in words:
            fmap[word] = fmap.get(word, 0) + 1
        
        nmap = {i:[] for i in range(len(words))}

        for word in fmap:
            nmap[fmap[word]].append(word)

        for i in range(len(words)-1, -1, -1):
            for word in nmap[i]:
                res.append(word)
                k -= 1
                if k == 0: return res
        
