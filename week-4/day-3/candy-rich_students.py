students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]


def candycounter(students):
    students_at_least_4_candies = 0
    for i in students:
        if i['candies'] > 4:
            students_at_least_4_candies += 1
    return students_at_least_4_candies

print(candycounter(students))
