a = 0

while a < 100:

    if a % 15 == 0:
        print('fizzbuzz')
        a += 1

    elif a % 3 == 0:
        print('fizz')
        a += 1

    elif a % 5 == 0:
        print('buzz')
        a += 1

    else:
        print(a)
        a += 1
