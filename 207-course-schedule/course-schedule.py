class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        cycle = set()
        finished = set()

        for course, pre in prerequisites:
            adj_list[course].append(pre)
        
        def dfs(node):
            if node in cycle: return False
            if adj_list[node] == []: return True
            if node in finished: return True
            # Process node
            cycle.add(node)
            for pre in adj_list[node]:
                if not dfs(pre): return False
            
            cycle.remove(node)
            finished.add(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True