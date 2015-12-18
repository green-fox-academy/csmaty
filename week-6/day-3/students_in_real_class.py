class Student():
    def __init__(self, name, grades):
        self.grades = grades
        self.name = name

    def add_grade(self, grade):
        if grade not in (1,5):
            return 'Wrong number'
        else:
            self.grades.append(grade)
            return self.grades

    def average(self):
        return sum(self.grades) / len(self.grades)

class Schoolclass():
    def __init__(self, studentlist):
        self.studentlist = studentlist
        self.sum_of_averages = 0
        self. namelist = []

    def calculate_wholeclass_average(self):
        self.average = 0
        for student in self.studentlist:
            self.sum_of_averages += student.average()
        return self.sum_of_averages / len(self.studentlist)

    # def get_average(self):
    #     return sum(map(lambda s: s.get_average, self.students())) / len(self.studentlist)

    def namelister(self):
        for student in self.studentlist:
            self.namelist.append(student.name)
        return ', '.join(self.namelist)

    # def lambdanamelister():
    #     return list(map(lambda s: s.name, self.students))

students_list = [
        Student('Egyeske', [2, 4, 4, 3]),
        Student('Ketteske', [2, 5, 4, 3]),
        Student('Harmaska', [2, 4, 1, 3])
        ]
wholeclass = Schoolclass(students_list)


print(wholeclass.calculate_wholeclass_average())
# print(wholeclass.get_average())
print(wholeclass.namelister())
# print(wholeclass.lambdanamelister())
