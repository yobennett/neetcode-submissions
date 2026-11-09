from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        queue = deque(students)

        # start with all n students
        result = n

        for sandwich in sandwiches:
            # for tracking if we've rotated through all students
            count = 0
            
            # rotate students in the queue until we find sandwich to match student
            # or until we've rotated all remaining students
            while count < n and queue[0] != sandwich:
                student = queue.popleft()
                queue.append(student)
                count += 1

            # found matching sandwich for student
            if queue[0] == sandwich:
                queue.popleft()
                result -= 1
            else:
                # no one wants the current sandwich after full rotation,
                # stop the process
                break

        return result