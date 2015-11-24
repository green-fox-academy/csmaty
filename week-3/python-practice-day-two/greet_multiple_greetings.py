def greet(name, greeting):
    if greeting is None:
        greeting = 'Hello, '
        print(greeting + name + '!')
    else:
        print(greeting + name + '!')

greet('Kati', 'Csa, ')
greet('Kati', None)


def greet(name, greeting = 'Hello!, '):
    print(greeting + name + '!')

def add(a, b, res = None):
    if res is None:
        res = res[]
        r = a + b
        res.append(r)
        print(res)
        return r

add(1, 2)
add(2, 3)
add(4, 5)
