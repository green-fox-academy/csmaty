i = 1
j = 1
fibonaccilist = []

fibonaccilist.append(i)
fibonaccilist.append(j)

for f in range(0,101):
    f = i + j
    fibonaccilist.append(f)
    i = j
    j = f
else:
    print(fibonaccilist)
