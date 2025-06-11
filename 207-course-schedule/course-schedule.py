class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        cycle = set()
        finished = set()

        for course, pre in prerequisites:
            adj_list[course].append(pre)

        def dfs(course):
            if course in cycle: return False
            if course in finished: return True

            cycle.add(course)
            for pre in adj_list[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            finished.add(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        