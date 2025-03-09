class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        adj_list = { i:[] for i in range(n)}
        visited= set()
        # Want no cycles

        for x,y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for x in adj_list[node]:
                if x == parent:
                    continue
                if dfs(x, node) == False:
                    return False
            

        if dfs(0,-1) == False: return False
        return True if len(visited) == n else False