class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}

        # prereq
        # ex. [0, 1] means 1 required before 0

        # initialize
        for i in range(numCourses):
            prereqs[i] = set()
        for course, prereq in prerequisites:
            prereqs[course].add(prereq)

        visiting = set()
        def dfs(course):
            # already visiting, cycle detected
            if course in visiting:
                return False
            # no prereqs, course can be completed
            if len(prereqs[course]) == 0:
                return True

            visiting.add(course)

            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            # remove prereqs for course, all can be completed
            prereqs[course] = [] 

            visiting.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True