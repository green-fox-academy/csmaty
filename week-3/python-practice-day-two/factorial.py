def factor(n):
    if n == 1:
        return 1
    else:
        return n * factor(n-1)

res = factor(4)
print (res)
