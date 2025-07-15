class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        finished = set()
        res = []
        adj_list = { i:[] for i in range(numCourses) }

        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        def dfs(node):
            if node in cycle: return False
            if node in finished: return True
            cycle.add(node)
            for pre in adj_list[node]:
                if not dfs(pre): return False
            cycle.remove(node)
            adj_list[node] = []
            res.append(node)
            finished.add(node)
            return True
        for i in range(numCourses):
            if i not in finished and not dfs(i): return []
        return res