class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj_list = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        edge_count = {}
        leaves = deque()
        for node, neighbors in adj_list.items():
            if len(neighbors) == 1:
                leaves.append(node)
            edge_count[node] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbor in adj_list[node]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)