class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = { i:[] for i in range(numCourses) }
        visited = set()

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        def topSort(node):
            if adj_list[node] == []: # no dependencies
                return True
            if node in visited:     # Circular dependency
                return False

            # Node not seen, and has neighbors -> Now do stuff
            visited.add(node)
            for prereq in adj_list[node]:
                if topSort(prereq) == False:
                    return False
            # Remove so that other nodes dont trigger false for a node that was actually true
            # visited.remove(node)
            adj_list[node] = []
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if topSort(i) == False:
                    return False
        
        return True

        