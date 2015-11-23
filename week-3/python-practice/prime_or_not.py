i = 9
d = 2


for d in range(2,i):
    if i % d == 0:
        print('it\'s NOT a prime number!')
        break

else:
    print('it\'s a prime number!')
