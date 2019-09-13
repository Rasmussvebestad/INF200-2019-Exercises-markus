# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 08:53:54 2019

@author: MarkusOla

__author__ = 'Markus Ola Granheim'
__email__ = 'mgranhei@nmbu.no'


"""
SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop(SUITS, VALUES):
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
            return deck


def deck_comp(SUITS, VALUES):
    return [(suit, val) for suit in SUITS for val in VALUES]


if deck_comp == 'deck_loop':
    if deck_loop() != deck_comp():
        print('ERROR!')

# %%  Oppgave 2:

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def comp_by_loop(n):
    new_list = []

    for k in range(len(n)):
        if k % 3 == 1:
            new_list.append(n[k] ** 2)

    return (new_list)


def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


if comp_by_loop(n) != squares_by_comp(n):
    print('ERROR!')

# %%

print(7 % 3)

# %%
a = 'ZENOVW'
txt = ''.join(sorted(a))


# %%
def letter_freq(txt):
    tekst = txt.lower()
    tekst = ''.join(sorted(tekst))

    all_freq = {}

    for bokstav in tekst:
        if bokstav in all_freq:
            all_freq[bokstav] += 1
        else:
            all_freq[bokstav] = 1
    return all_freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')
    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))

# %%

txt = 'banana'

print(txt[1])
print
count_letters('banana', 'a')

pass

if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))

from random import randint as a


def b():
    c = 0
    while c < 1:
        c = int(input('Your guess: '))
    return c


def d():
    return a(1, 6) + a(1, 6)


def e(f, g):
    return f == g


if __name__ == '__main__':

    h = False
    i = 3
    j = d()
    while not h and i > 0:
        k = b()
        h = e(j, k)
        if not h:
            print('Wrong, try again!')
            i -= 1

    if i > 0:
        print('You won {} points.'.format(i))
    else:
        print('You lost. Correct answer: {}.'.format(j))

