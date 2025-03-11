class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}

        for a,b in roads:
            adj_list[a].append(b)
            adj_list[b].append(a)

        
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                cur = len(adj_list[i]) + len(adj_list[j])
                if i in adj_list[j]:
                    cur -= 1
                res = max(res, cur)

        return res