students = [
    {'name': 'Tibi', 'age': 8},
    {'name': 'Adorjan', 'age': 9},
    {'name': 'Agoston', 'age': 6},
    {'name': 'Aurel', 'age': 7},
    {'name': 'Dezso', 'age': 12},
]

students_at_least_8 = []
studentsnamestartswitha = []

def studentagefilter(student):
    for i in students:
            if i['age'] >= 8:
                students_at_least_8.append(i['name'])

    return students_at_least_8

def studentnamefilter(student):

    for i in students:
        if i['name'][0] == 'A':
            studentsnamestartswitha.append(i['age'])
    return studentsnamestartswitha

print(studentagefilter(students))
print(studentnamefilter(students))
