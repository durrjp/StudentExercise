CREATE TABLE StudentExercise(
    Id integer not null primary key AUTOINCREMENT,
    StudentId integer not null,
    ExerciseId integer not null,
    foreign key(StudentId) REFERENCES Student(Id),
    foreign key(ExerciseId) REFERENCES Exercise(Id)
)