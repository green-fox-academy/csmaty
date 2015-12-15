class Student():
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        if grade not in (1,5):
            return 'Wrong number'
        else:
            self.grades.append(grade)
            return self.grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student([2, 4, 4, 3])
print(student.add_grade(5))
print(student.add_grade(0))
print(student.add_grade(6))
print(student.average())
