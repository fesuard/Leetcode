# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description
# We have a queue of students with their sandwich preferences and a stack of sandwiches
# to be served. The goal is to serve sandwiches to students based on their preferences.
# If a student's preferred sandwich is available, serve it; otherwise, move to the next 
# student. The process stops when all sandwiches are served or when there are no more
# students to serve.


# Brut force approach, we simulate each step until the sandwich type does not match
# any of the remaining students or until the sandwiches list is empty. We return the
# length of the remaining students, since they will be the ones that won't eat.
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while sandwiches:
            if sandwiches[0] not in students:
                break
            
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            
            else:
                moved_student = students.pop(0)
                students.append(moved_student)
            
        return len(students)


# Optimized solution, we count the number of students for each preferrence, then
# we iterate only once through the sandwiches, we decrement count when the student
# matches the sandwich type until there are no remaining students or until the 
# sandwich type cannot match any of the students.
class Solution1:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {
            0: 0,
            1: 0
        }
        remaining = len(students)

        for student in students:
            count[student] += 1

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break
            if remaining == 0:
                break
            count[sandwich] -= 1
            remaining -= 1

        return remaining
      
