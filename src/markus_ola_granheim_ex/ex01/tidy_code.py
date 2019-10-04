"""
Koden kaster to terninger (summerer to tilfeldige verdier mellom 1 og 6).
Såhar du tre forsøk på å gjette verdien.
Der du får flere poeng desto færre forsøk du bruker.
"""
from random import randint


def your_guess():
    c = 0
    while c < 1:
        c = int(input('Your guess: '))
    return c


def sum_of_dices():
    return randint(1, 6) + randint(1, 6)


def if_correct_guess(f, g):
    return f == g


if __name__ == '__main__':
    checking_answer = False  # checking if wrong answer
    number_of_tries = 3  # also number of points
    correct_answer = sum_of_dices()
    while not checking_answer and number_of_tries > 0:
        yourguess = your_guess()
        checking_answer = if_correct_guess(correct_answer, yourguess)

        if not checking_answer:
            print('Wrong, try again!')
            number_of_tries -= 1

    if number_of_tries > 0:
        print('You won {} points.'.format(number_of_tries))
    else:
        print('You lost. Correct answer: {}.'.format(correct_answer))


