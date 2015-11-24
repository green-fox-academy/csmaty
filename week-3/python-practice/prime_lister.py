primelist = []

for i in range(2,100):
    for d in range(2,i):
       if (i % d) == 0:
           break
    else:
       primelist.append(i)

print(primelist)
