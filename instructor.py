from student import Student
from exercise import Exercise

class Instructor:
    def __init__(self, firstName, lastName, slack, cohort, specialty):
        self.firstName = firstName
        self.lastName = lastName
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty
    def studentAssign(self, student, exercise):
        student.exerciseCol.append(exercise)
        

        