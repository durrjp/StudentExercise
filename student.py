from person import Person

class Student(Person):
    def __init__(self, firstName, lastName, slack, cohort):
        super().__init__(firstName, lastName, slack, cohort)
        self.exerciseCol = []

    def listExercises(self):
        for exercise in self.exerciseCol:
            return exercise.name