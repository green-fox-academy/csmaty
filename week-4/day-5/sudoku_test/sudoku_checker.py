def is_complete(numbers):
    if len(numbers) != 9:
        return False

def is_too_long(numbers):
    if len(numbers) > 9:
        return False

def repeating_numbers(numbers):
    if len(numbers) != len(set(numbers)):
        return False

def not_1_through_9(numbers):
    if numbers.sort() != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False
