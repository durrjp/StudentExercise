from student import Student
from exercise import Exercise
from instructor import Instructor
from cohort import Cohort

exercise1 = Exercise("python classes", "python")
exercise2 = Exercise("C# classes", "C#")
exercise3 = Exercise("Java classes", "Java")
exercise4 = Exercise("React state", "React/Javascript")

cohort39 = Cohort("Cohort 39")
cohort40 = Cohort("Cohort 40")
cohort41 = Cohort("Cohort 41")

joe = Student("Joe", "Shmoe", "joeshmo", cohort39)
jane = Student("Jane", "Fonda", "janef", cohort39)
sally = Student("Sally", "Fields", "sallyf", cohort40)
bill = Student("Bill", "Bo", "billbo", cohort41)

profSteve = Instructor("Steve", "Brownlee", "coach", cohort39, "Dad jokes")
profAndy = Instructor("Andy", "Collins", "andyc", cohort40, "C#")
profAdam = Instructor("Adam", "Scheaffer", "adamsh", cohort41, "Memes")

profSteve.studentAssign(joe, exercise1)
profSteve.studentAssign(joe, exercise2)

profSteve.studentAssign(jane, exercise3)
profSteve.studentAssign(jane, exercise4)

profAndy.studentAssign(sally, exercise2)
profAndy.studentAssign(sally, exercise4)

profAdam.studentAssign(bill, exercise1)
profAdam.studentAssign(bill, exercise3)

students = list()
students.append(joe)
students.append(jane)
students.append(sally)
students.append(bill)

exercises = list()
exercises.append(exercise1)
exercises.append(exercise2)
exercises.append(exercise3)
exercises.append(exercise4)

def reportBuilder():
    for student in students:
        exercises = list()
        for exercise in student.exerciseCol:
            exercises.append(exercise.name)
        stringEx = " and ".join(exercises)
        print(f"{student.firstName} is working on {stringEx}")

reportBuilder()
