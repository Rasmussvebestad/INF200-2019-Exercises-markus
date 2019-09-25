import collections
import math as m


def letter_freq(txt):
    streng = txt.lower()
    streng = ''.join(sorted(streng))
    tekst = collections.OrderedDict()

    for symbol in streng:
        if symbol in tekst:
            tekst[symbol] += 1
        else:
            tekst[symbol] = 1
    return tekst


def entropy(text=input('Please enter text to analyse: ')):
    tekst = letter_freq('message')
    dict_keys = list(tekst.values())
    n = len(text)
    totalt = 0

    for i in range(len(dict_keys)):
        totalt += ((dict_keys[i] / n) * m.log2(dict_keys[i] / n))

    return totalt

    pass
