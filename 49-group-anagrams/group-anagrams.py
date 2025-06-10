class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a fmap of the str[i]
        # use that fmap as a key to look in the result array and append

        # or sort each str[i] and then sort as items will be the same


        res = {}

        for s in strs:
            tmp = ''.join(sorted(s))
            print(tmp)
            if tmp not in res:
                res[tmp] = []
            res[tmp].append(s)
        return list(res.values())