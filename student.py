class Student:
    def __init__(self, firstName, lastName, slack, cohort):
        self.firstName = firstName
        self.lastName = lastName
        self.slack = slack
        self.cohort = cohort
        self.exerciseCol = []

    def listExercises(self):
        for exercise in self.exerciseCol:
            return exercise.name