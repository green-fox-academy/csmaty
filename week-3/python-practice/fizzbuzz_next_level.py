a = 0

while a < 100:
    if '3' in str(a) and '5' in str(a) or a % 15 == 0:
        print('fizzbuzz')
        a += 1

    elif '3' in str(a) or a % 3 == 0:
        print ('fizz')
        a += 1

    elif '5' in str(a) or a % 5 == 0:
        print ('buzz')
        a += 1
    else:
        print(a)
        a += 1
