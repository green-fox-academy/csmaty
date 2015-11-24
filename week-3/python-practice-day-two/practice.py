numbers = [1, 2, 7, 6, 5]

maximum = numbers[0]
i = 0

while i < len(numbers):
    if maximum < numbers[i]:
        maximum = numbers[i]
    i += 1
print(maximum)
