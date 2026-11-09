class Solution:
    # Topological sort with DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # Store courses visiting along a path during DFS
        visiting = set()

        def dfs(course):
            # Cycle detected
            if course in visiting:
                return False

            # No prereqs, can finish by default
            if len(adj[course]) == 0:
                return True

            # Add course to visiting set
            visiting.add(course)

            for prereq in adj[course]:
                # prereq cannot be finished
                if not dfs(prereq):
                    return False

            # cleanup
            # Remove course from visiting set
            visiting.remove(course)
            # Set prereqs to empty, all prereqs can be finished
            adj[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True