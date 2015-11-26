from random import randint

number_of_guesses = 5
number_to_guess = randint(0, 10)

def get_integer():
    number = int(input("Enter an integer: "))
    return number


while number_of_guesses > 0:

    try:
        number = get_integer()
    except ValueError:
        print("You entered a wrong value")
    else:

        if number < number_to_guess:
            print('The number I thought of is bigger')
            number_of_guesses -= 1

        elif number > number_to_guess:
            print ('The number I thought of is smaller')
            number_of_guesses -= 1

        else:
            print("Congratulations!! You guessed my number!")
            break
