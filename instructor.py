from student import Student
from exercise import Exercise
from person import Person

class Instructor(Person):
    def __init__(self, firstName, lastName, slack, cohort, specialty):
        super().__init__(firstName, lastName, slack, cohort)
        self.specialty = specialty
    def studentAssign(self, student, exercise):
        student.exerciseCol.append(exercise)
        

        