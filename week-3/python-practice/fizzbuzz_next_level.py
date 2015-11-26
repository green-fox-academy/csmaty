a = 0

while a < 100:
    if '3' in str(a) and '5' in str(a) or a % 15 == 0:
        print('fizzbuzz')

    elif '3' in str(a) or a % 3 == 0:
        print ('fizz')

    elif '5' in str(a) or a % 5 == 0:
        print ('buzz')
    else:
        print(a)
a += 1
