def even_numbers(numbers):
    output = []
    for i in numbers:
        if i % 2 == 0:
            output.append(i)
    print(output)

even_numbers([1, 2, 3, 4, 5, 6, 7, 8])
