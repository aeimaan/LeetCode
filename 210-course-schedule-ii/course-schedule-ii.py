class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = { i:[] for i in range(numCourses) }
        cycle = set()
        res = []

        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        def dfs(node):
            if node in cycle: return False
            if adj_list[node] == []:
                if node not in res: res.append(node)
                return True
            cycle.add(node)
            for pre in adj_list[node]:
                if not dfs(pre): return False
            cycle.remove(node)
            adj_list[node] = []
            if node not in res: res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return list(res)
