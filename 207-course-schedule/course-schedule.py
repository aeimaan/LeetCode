class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Want to detect that there are no cycles in ths graph

        adj_list = { i:[]  for i in range(numCourses)}
        cycle = set()
        visited = set()

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)
            for prereq in adj_list[node]:
                if dfs(prereq) == False:
                    return False
            
            cycle.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True