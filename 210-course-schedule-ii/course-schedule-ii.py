class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        res = []
        visited = set()
        cycle = set()

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            # if adj_list[node] == []:
            #     res.append(node)
            #     visited.add(node)
            #     return True
            
            cycle.add(node)
            for pre in adj_list[node]:
                if dfs(pre) == False:
                    return False
            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if dfs(i) == False:
                    return []
        
        return res
        
