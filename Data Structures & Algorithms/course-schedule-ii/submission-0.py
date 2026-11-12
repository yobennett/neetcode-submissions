class Solution:
    # Topological sort, with DFS and cycle detection
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # setup
        adj = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # initialize
        visit, cycle = set(), set()

        result = []

        def dfs(course):
            # cycle detected
            if course in cycle:
                return False
            # skip, already visiting in current path
            if course in visit:
                return True

            # track
            cycle.add(course)

            # DFS prereqs
            for prereq in adj[course]:
                if dfs(prereq) == False:
                    return False

            # cleanup
            cycle.remove(course)
            visit.add(course)

            result.append(course)
            return True

        # DFS for each course
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result