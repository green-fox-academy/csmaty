
def adder(array):
    """new_array = []
    for i in array:
        new_array.append(i + 1)
    return new_array"""

    """def add(n):
        return n + 1
    return list(map(add, array))"""

    return list(map(lambda x: x+1, array))

def filter_array(array):
    return list(filter(lambda x: x % 3 == 0, array))
