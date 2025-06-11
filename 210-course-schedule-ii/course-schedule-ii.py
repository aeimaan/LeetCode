class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}
        cycle = set()
        finished = set()
        res = []

        for course, pre in prerequisites:
            adj_list[course].append(pre)

        def dfs(node):
            if node in cycle: return False
            if node in finished: 
                return True
            cycle.add(node)
            for pre in adj_list[node]:
                if not dfs(pre): return False
            cycle.remove(node)
            finished.add(node)
            res.append(node)
            adj_list[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return []

        return res
